# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('climbgupiao', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankuailist',
            name='id',
        ),
        migrations.AlterField(
            model_name='bankuailist',
            name='name',
            field=models.CharField(max_length=15, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
