# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('figshare', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='figshare',
            name='resource_doi',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='figshare',
            name='resource_link',
            field=models.URLField(blank=True),
        ),
    ]
