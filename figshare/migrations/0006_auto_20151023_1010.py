# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('figshare', '0005_pubsearch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pubsearch',
            name='date_from',
            field=models.DateField(help_text=b'Date format is: 2015-12-25 (YYYY-MM-DD)', verbose_name=b'Search From', blank=True),
        ),
        migrations.AlterField(
            model_name='pubsearch',
            name='date_to',
            field=models.DateField(help_text=b'Date format is: 2015-12-25 (YYYY-MM-DD)', verbose_name=b'Search to', blank=True),
        ),
        migrations.AlterField(
            model_name='pubsearch',
            name='has_author',
            field=models.CharField(default=b'', max_length=80, verbose_name=b'Author', blank=True),
        ),
        migrations.AlterField(
            model_name='pubsearch',
            name='has_category',
            field=models.CharField(default=b'', max_length=80, verbose_name=b'Category', blank=True),
        ),
        migrations.AlterField(
            model_name='pubsearch',
            name='has_tag',
            field=models.CharField(default=b'', max_length=80, verbose_name=b'Tag', blank=True),
        ),
        migrations.AlterField(
            model_name='pubsearch',
            name='has_title',
            field=models.CharField(default=b'', max_length=80, verbose_name=b'Title', blank=True),
        ),
        migrations.AlterField(
            model_name='pubsearch',
            name='search_for',
            field=models.CharField(default=b'', help_text=b'Please enter key phrase', max_length=80, verbose_name=b'Search Query'),
        ),
    ]
