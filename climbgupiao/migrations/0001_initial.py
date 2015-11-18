# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bankuailist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15)),
                ('daima', models.CharField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='gupiaolist',
            fields=[
                ('symbol', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=15)),
                ('sybk', models.CharField(default=b'\xe6\x9c\xaa\xe7\x9f\xa5', max_length=15)),
                ('current', models.FloatField(default=0)),
                ('marketCapital', models.FloatField(default=0)),
                ('pe_ttm', models.FloatField(default=0)),
                ('pe_lyr', models.FloatField(default=0)),
                ('pb', models.FloatField(default=0)),
                ('net_asset', models.FloatField(default=0)),
                ('gjj', models.FloatField(default=0)),
                ('netprofit', models.FloatField(default=0)),
                ('dilutedroe', models.FloatField(default=0)),
                ('netincgrowrate', models.FloatField(default=0)),
                ('totassgrowrate', models.FloatField(default=0)),
                ('salegrossprofitrto', models.FloatField(default=0)),
                ('mainbusiincome', models.FloatField(default=0)),
                ('test1', models.FloatField(default=0)),
                ('test2', models.FloatField(default=0)),
                ('test3', models.FloatField(default=0)),
                ('test4', models.FloatField(default=0)),
                ('test5', models.FloatField(default=0)),
                ('test6', models.FloatField(default=0)),
                ('test7', models.FloatField(default=0)),
                ('test8', models.FloatField(default=0)),
                ('test9', models.FloatField(default=0)),
                ('test10', models.FloatField(default=0)),
                ('shangshidays', models.IntegerField(default=0, max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
