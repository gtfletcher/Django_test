# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FigShare',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resource_name', models.CharField(max_length=80)),
                ('author_name', models.CharField(max_length=80)),
                ('resource_doi', models.URLField()),
                ('resource_link', models.URLField()),
            ],
        ),
    ]
