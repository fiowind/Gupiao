# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('climbgupiao', '0003_auto_20151117_0957'),
    ]

    operations = [
        migrations.CreateModel(
            name='bankuai',
            fields=[
                ('fenlei_name', models.CharField(max_length=15)),
                ('bankuai_name', models.CharField(max_length=15, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='bankuailist',
            old_name='daima',
            new_name='bankuai_name',
        ),
        migrations.AddField(
            model_name='bankuailist',
            name='code',
            field=models.CharField(default=b'0', max_length=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bankuailist',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=0, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bankuailist',
            name='name',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
    ]
