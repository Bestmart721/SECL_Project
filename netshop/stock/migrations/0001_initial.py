# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('adress', models.CharField(max_length=50)),
                ('city', models.ForeignKey(verbose_name='\u0433\u043e\u0440\u043e\u0434', to='place.City')),
            ],
            options={
                'verbose_name': '\u0441\u043a\u043b\u0430\u0434',
                'verbose_name_plural': '\u0441\u043a\u043b\u0430\u0434\u044b',
            },
        ),
    ]
