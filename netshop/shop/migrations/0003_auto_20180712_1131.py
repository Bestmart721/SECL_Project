# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20180712_1128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='type',
            new_name='type_of_shop',
        ),
    ]
