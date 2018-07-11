# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0001_initial'),
        ('stock', '0001_initial'),
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u043d\u0430\u0437\u0432\u0430')),
                ('website', models.URLField(blank=True)),
                ('city', models.ForeignKey(verbose_name='\u0433\u043e\u0440\u043e\u0434', to='place.City')),
                ('owner', models.ForeignKey(related_name='owner_shop', verbose_name='\u0432\u043b\u0430\u0434\u0435\u043b\u0435\u0446', to='person.Person')),
                ('seller', models.ManyToManyField(related_name='seller_shop', verbose_name='\u043f\u0440\u043e\u0434\u0430\u0432\u0446\u044b', to='person.Person')),
                ('stock', models.ManyToManyField(to='stock.Stock', verbose_name='\u0441\u043a\u043b\u0430\u0434\u044b')),
            ],
            options={
                'verbose_name': '\u043c\u0430\u0433\u0430\u0437\u0438\u043d',
                'verbose_name_plural': '\u043c\u0430\u0433\u0430\u0437\u0438\u043d\u044b',
            },
        ),
        migrations.CreateModel(
            name='TypeShop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u0442\u0438\u043f \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0430')),
            ],
            options={
                'verbose_name': '\u0442\u0438\u043f \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0430',
                'verbose_name_plural': '\u0442\u0438\u043f\u044b \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u043e\u0432',
            },
        ),
        migrations.AddField(
            model_name='shop',
            name='type_of_shop',
            field=models.ForeignKey(verbose_name='\u0442\u0438\u043f \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0430', to='shop.TypeShop'),
        ),
    ]
