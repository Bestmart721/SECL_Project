# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='\u043f\u043e\u043b', choices=[(0, '\u043c\u0443\u0436\u0441\u043a\u043e\u0439'), (1, '\u0436\u0435\u043d\u0441\u043a\u0438\u0439')]),
        ),
    ]
