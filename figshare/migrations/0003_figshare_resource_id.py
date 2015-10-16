# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('figshare', '0002_auto_20151015_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='figshare',
            name='resource_id',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
