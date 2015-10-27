# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('figshare', '0008_auto_20151023_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='figshare',
            name='json_file',
            field=models.FileField(default=b'', help_text=b'Please upload the json meta data file', verbose_name=b'JSON Meta Data File', upload_to=b'/json/%Y/%m/'),
        ),
    ]
