# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('figshare', '0006_auto_20151023_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='pubsearch',
            name='page_num',
            field=models.IntegerField(default=1, verbose_name=b'Results Page Number'),
        ),
    ]
