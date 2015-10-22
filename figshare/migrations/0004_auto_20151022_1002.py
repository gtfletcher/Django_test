# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('figshare', '0003_figshare_resource_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='figshare',
            name='resource_doi',
            field=models.URLField(default=b''),
        ),
        migrations.AlterField(
            model_name='figshare',
            name='resource_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='figshare',
            name='resource_link',
            field=models.URLField(default=b''),
        ),
    ]
