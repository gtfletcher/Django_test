# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('figshare', '0007_pubsearch_page_num'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pubsearch',
            old_name='page_num',
            new_name='page',
        ),
    ]
