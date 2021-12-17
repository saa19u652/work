# Generated by Django 3.1.6 on 2021-10-17 23:06

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import gallery.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, default='Сидоров Валентин Михайлович', max_length=100, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('located', models.CharField(max_length=100, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Место нахождения',
                'verbose_name_plural': 'Место нахождения',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=30, verbose_name='Материал')),
            ],
            options={
                'verbose_name': 'Материал',
                'verbose_name_plural': 'Материалы',
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=40, verbose_name='Владелец')),
            ],
            options={
                'verbose_name': 'Владелец',
                'verbose_name_plural': 'Владелецы',
            },
        ),
        migrations.CreateModel(
            name='Paints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paints', models.CharField(max_length=30, verbose_name='Техника')),
            ],
            options={
                'verbose_name': 'Техника',
                'verbose_name_plural': 'Техника',
            },
        ),
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signature', models.CharField(max_length=40, verbose_name='Подпись')),
            ],
            options={
                'verbose_name': 'Подпись',
                'verbose_name_plural': 'Подписи',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_art', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Идентификатор работы')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('year', models.CharField(blank=True, default='', max_length=30, verbose_name='Дата')),
                ('sizeW', models.FloatField(blank=True, default=0, verbose_name='Ширина (см)')),
                ('sizeH', models.FloatField(blank=True, default=0, verbose_name='Высота (см)')),
                ('picL', models.ImageField(blank=True, default='', upload_to=gallery.models.gallery_upload_to, verbose_name='Фотография картины')),
                ('picM', models.ImageField(blank=True, default='', upload_to=gallery.models.gallery_upload_to, verbose_name='Фотография подписи')),
                ('picS', models.ImageField(blank=True, default='', upload_to=gallery.models.gallery_upload_to, verbose_name='Фотография обратной стороны')),
                ('comment', models.TextField(blank=True, default='', verbose_name='Комментарий')),
                ('checked', models.BooleanField(default=False, verbose_name='Проверено')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gallery.author', verbose_name='Автор')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gallery.location', verbose_name='Место нахождения')),
                ('material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.material', verbose_name='Материал')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gallery.owner', verbose_name='Владелец')),
                ('paints', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.paints', verbose_name='Техника')),
                ('signature', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gallery.signature', verbose_name='Подпись')),
            ],
            options={
                'verbose_name': 'Картина',
                'verbose_name_plural': 'Картины',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
