# coding=utf-8
from django.db import models

class TypeShop(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'тип магазина')

    class Meta:
        verbose_name = u'тип магазина'
        verbose_name_plural = u'типы магазинов'

    def __unicode__(self):
        return u'тип магазина: {}'.format(self.name)

    @models.permalink
    def get_absolute_url(self):
        return 'type_detail', (), {'pk': self.pk}

class Shop(models.Model):
    type_of_shop = models.ForeignKey('TypeShop', verbose_name=u'тип магазина')
    name = models.CharField(max_length=50, verbose_name=u'назва')
    owner = models.ForeignKey('person.Person', verbose_name=u'владелец', related_name='owner_shop')
    seller = models.ManyToManyField('person.Person', verbose_name=u'продавцы', related_name='seller_shop')
    stock = models.ManyToManyField('stock.Stock', verbose_name=u'склады')
    city = models.ForeignKey('place.City', verbose_name=u'город')
    website = models.URLField(blank=True)

    class Meta:
        verbose_name = u'магазин'
        verbose_name_plural = u'магазины'

    def __unicode__(self):
        return u'Магазин {}'.format(self.name)

    def description(self):
        return u'{} расположен в {}, {}'.format(self.name, self.city, self.type_of_shop)

    @models.permalink
    def get_absolute_url(self):
        return 'shop_detail', (), {'pk': self.pk}