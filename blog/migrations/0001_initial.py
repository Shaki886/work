# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Tytul', models.CharField(max_length=200)),
                ('Marka', models.TextField(verbose_name=50)),
                ('Model', models.TextField(verbose_name=50)),
                ('Rok', models.IntegerField(verbose_name=4)),
                ('Stan', models.TextField(default='uzywany')),
                ('Przebieg', models.IntegerField(verbose_name=50)),
                ('zdjecie', models.FileField(upload_to='')),
                ('Opis', models.TextField(verbose_name=500)),
                ('data_utworzenia', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_publikacji', models.DateTimeField(null=True, blank=True)),
                ('Login', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Kategorie_aut',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nazwa_kategorii', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='kategoria',
            field=models.ForeignKey(to='blog.Kategorie_aut'),
        ),
    ]
