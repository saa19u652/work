from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


class Signature(models.Model):
    signature = models.CharField(max_length=40, verbose_name='Подпись')

    def __str__(self):
        return self.signature

    class Meta:
        verbose_name = 'Подпись'
        verbose_name_plural = 'Подписи'


class Material(models.Model):
    material = models.CharField(max_length=30, verbose_name='Материал')

    def __str__(self):
        return self.material

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'


class Location(models.Model):
    located = models.CharField(max_length=100, verbose_name='Адрес')

    def __str__(self):
        return self.located

    class Meta:
        verbose_name = 'Место нахождения'
        verbose_name_plural = 'Место нахождения'


def gallery_upload_to(instance, filename):
    return './gallery_pic/{}{}/{}'.format(datetime.now().year, datetime.now().month, filename)


class Paints(models.Model):
    paints = models.CharField(max_length=30, verbose_name='Техника')

    def __str__(self):
        return self.paints

    class Meta:
        verbose_name = 'Техника'
        verbose_name_plural = 'Техника'


class Owner(models.Model):
    owner = models.CharField(max_length=40, verbose_name='Владелец')

    def __str__(self):
        return self.owner

    class Meta:
        verbose_name = 'Владелец'
        verbose_name_plural = 'Владелецы'


class Author(models.Model):
    author = models.CharField(max_length=100, verbose_name='Автор', default='', blank=True)

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class GalleryManager(models.Manager):
    def getAllArt(self):
        return self.all()


class Gallery(models.Model):
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, verbose_name="Автор",  null=True, blank=True)
    id_art = models.CharField(max_length=100, verbose_name="Идентификатор работы", default='', blank=True, null=True)
    title = models.CharField(max_length=100, verbose_name='Название', null=False)
    year = models.CharField(max_length=30, verbose_name='Дата',  default='', blank=True)
    material = models.ForeignKey('Material', on_delete=models.CASCADE, verbose_name="Материал", null=True, blank=True)
    paints = models.ForeignKey('Paints', on_delete=models.CASCADE, verbose_name="Техника",  null=True, blank=True)
    sizeW = models.FloatField(verbose_name='Ширина (см)',  default=0, blank=True)
    sizeH = models.FloatField(verbose_name='Высота (см)',  default=0, blank=True)
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, verbose_name="Место нахождения",  null=True, blank=True)
    owner = models.ForeignKey('Owner', on_delete=models.SET_NULL, verbose_name="Владелец",  null=True, blank=True)
    picL = models.ImageField(verbose_name="Фотография картины", upload_to=gallery_upload_to, default='', blank=True)
    picM = models.ImageField(verbose_name="Фотография подписи", upload_to=gallery_upload_to, default='', blank=True)
    picS = models.ImageField(verbose_name="Фотография обратной стороны", upload_to=gallery_upload_to, default='', blank=True)
    comment = models.TextField(verbose_name="Комментарий", default='', blank=True)
    signature = models.ForeignKey('Signature', on_delete=models.DO_NOTHING, verbose_name="Подпись",  null=True, blank=True)
    checked = models.BooleanField(verbose_name="Проверено", default=False)
    object = GalleryManager()

    def image_tag(self):
        if self.picS:
            print(self.picS.url[12:])
            return mark_safe('<img src="%s" style="width: 100px; height: 100px; object-fit: contain;" />' % self.picS.url)
        else:
            return 'No Image Found'

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Картина'
        verbose_name_plural = 'Картины'
