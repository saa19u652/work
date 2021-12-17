# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u7746268/data/www/vmsidorov.ru/work')
sys.path.insert(1, '/var/www/u7746268/data/djangoenv/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'work.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

