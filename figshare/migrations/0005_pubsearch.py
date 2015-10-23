# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('figshare', '0004_auto_20151022_1002'),
    ]

    operations = [
        migrations.CreateModel(
            name='PubSearch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('search_for', models.CharField(default=b'', max_length=80)),
                ('date_from', models.DateField(blank=True)),
                ('date_to', models.DateField(blank=True)),
                ('has_author', models.CharField(default=b'', max_length=80, blank=True)),
                ('has_title', models.CharField(default=b'', max_length=80, blank=True)),
                ('has_category', models.CharField(default=b'', max_length=80, blank=True)),
                ('has_tag', models.CharField(default=b'', max_length=80, blank=True)),
            ],
        ),
    ]
