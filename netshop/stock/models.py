# coding=utf-8
from django.db import models

class Stock(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'название')
    city = models.ForeignKey('place.City', verbose_name=u'город')
    adress = models.CharField(max_length=50)

    class Meta:
        verbose_name = u'склад'
        verbose_name_plural = u'склады'

    def __unicode__(self):
        return u'Название: {}'.format(self.name)

    def description(self):
        return self

    def get_address(self):
        return u'адрес: {}'.format(self.adress)

    @models.permalink
    def get_absolute_url(self):
        return 'stock_detail', (), {'pk': self.pk}

    # def get_absolute_url(self):
    #     return "shop/%s/" % (self.id)