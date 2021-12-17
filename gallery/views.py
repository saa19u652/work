import os
from functools import reduce
from glob import glob

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML
from gallery.forms import LoginForm
from django.contrib import auth
from gallery.models import *
import numpy as np
from pathlib import Path

from django.contrib.admin.utils import flatten


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.user.is_authenticated:
        return redirect(overview)
    if request.method == "GET":
        form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = auth.authenticate(request, **form.cleaned_data)
            if user is not None:
                auth.login(request, user)
                return redirect(request.GET.get("next", "/"))
            else:
                form.add_error('password', 'Неверный логин или пароль')

    ctx = {'form': form}
    return render(request, 'login.html', ctx)


def paginator(data, request, pages=10):
    obj_paginator = Paginator(data, pages)
    page = request.GET.get('page')
    obj_paginator = obj_paginator.get_page(page)
    return obj_paginator


@login_required
def overview(request):
    data = paginator(Gallery.object.all().order_by('-id'), request)
    return render(request, 'overview.html', {
        'data': data,
        'material': Material.objects.all(),
        'tech': Paints.objects.all(),
        'places': Location.objects.all(),
        'owner': Owner.objects.all()
    })


def logout(request):
    auth.logout(request)
    return redirect("/")


@require_POST
def filter_data(request):
    material = request.POST.getlist('materail[]')
    paints = request.POST.getlist('tech[]')
    place = request.POST.getlist('location[]')
    owner = request.POST.getlist('owner[]')
    offest = request.POST.get('offset', 0)
    if offest == '':
        offest = 0
    else:
        offest = int(offest)

    width_from = request.POST.get('wfrom', 0)
    if width_from == '':
        width_from = 0
    else:
        width_from = float(width_from)

    width_to = request.POST.get('wto', 9999)
    if width_to == '':
        width_to = 9999
    else:
        width_to = float(width_to)

    hieght_from = request.POST.get('hfrom', 0)
    if hieght_from == '':
        hieght_from = 0
    else:
        hieght_from = float(hieght_from)

    hieght_to = request.POST.get('hto', 9999)
    if hieght_to == '':
        hieght_to = 9999
    else:
        hieght_to = float(hieght_to)

    date_from = request.POST.get('date_from', 0)
    if date_from == '':
        date_from = 0
    else:
        date_from = date_from

    date_to = request.POST.get('date_to', 9999)
    if date_to == '':
        date_to = 9999
    else:
        date_to = date_to

    limit = 10
    query = Gallery.object.filter()
    title = request.POST.get('title', '')
    if title != '':
        query = query.filter(title__contains=title)

    query = query.filter(sizeW__gte=width_from, sizeW__lte=width_to).filter(sizeH__gte=hieght_from,
                                                                            sizeH__lte=hieght_to)
    print(len(material))
    if np.array(material).size > 0:
        material = reduce(lambda x, y: x | y, [Q(material__material=item) for item in material])
        query = query.filter(material)
    if np.array(paints).size > 0:
        paints = reduce(lambda x, y: x | y, [Q(paints__paints=item) for item in paints])
        query = query.filter(paints)
    if np.array(place).size > 0:
        place = reduce(lambda x, y: x | y, [Q(location__located=item) for item in place])
        query = query.filter(place)
    if np.array(owner).size > 0:
        owner = reduce(lambda x, y: x | y, [Q(owner__owner=item) for item in owner])
        query = query.filter(owner)
    query = query.order_by("-id")
    array = query[offest:limit + offest]
    if request.user.groups.first().name == "visitor":
        data = list(
            array.values('pk', 'author__author', 'title', 'year', 'material__material', 'paints__paints', 'sizeW', 'sizeH',
                         'picS'))
    else:
        data = list(
            array.values('pk', 'author__author', 'title', 'year', 'material__material', 'paints__paints', 'sizeW', 'sizeH',
                         'location__located', 'owner__owner', 'picL', 'picM', 'picS'))
    return JsonResponse(data={
        'post': data,
        'totalResult': query.count()
    }, safe=False)


@login_required
def art(request, id):
    data = Gallery.object.get(pk=id)
    print(data)
    return render(request, 'art.html', {
        'data': data,
    })


@login_required
def write_pdf_view(request):
    html_string = render_to_string('pdf_template.html',
                                   {'art': Gallery.object.filter(Q(location__id=1))})
    html = HTML(string=html_string, base_url='')
    html.write_pdf(target='/tmp/mypdf.pdf');

    fs = FileSystemStorage('/tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'
        response['Content-Transfer-Encoding'] = 'binary'
        return response

    return response
