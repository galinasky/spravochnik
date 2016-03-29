# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_name', models.CharField(max_length=100, verbose_name=b'\xd1\x84\xd0\xb0\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x8f')),
                ('first_name', models.CharField(max_length=100, verbose_name=b'\xd0\xb8\xd0\xbc\xd1\x8f')),
                ('e_mail', models.EmailField(max_length=100, verbose_name=b'\xd0\xbf\xd0\xbe\xd1\x87\xd1\x82\xd0\xb0')),
                ('telephon', models.IntegerField(max_length=10, verbose_name=b'\xd1\x82\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd')),
                ('doljn', models.CharField(max_length=200, verbose_name=b'\xd0\xb4\xd0\xbe\xd0\xbb\xd0\xb6\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c')),
            ],
            options={
                'ordering': ['last_name', 'doljn'],
            },
        ),
    ]
