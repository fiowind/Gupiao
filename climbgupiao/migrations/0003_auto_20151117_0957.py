# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('climbgupiao', '0002_auto_20151116_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='gupiaolist',
            name='netprofit_jd1',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gupiaolist',
            name='netprofit_jd2',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gupiaolist',
            name='netprofit_jd3',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gupiaolist',
            name='netprofit_nd1',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gupiaolist',
            name='netprofit_nd2',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gupiaolist',
            name='netprofit_nd3',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
