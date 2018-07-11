# coding=utf-8

from django.db import models

# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'название')
    city = models.ForeignKey('place.City', verbose_name=u'город')
    adress = models.CharField(max_length=50)

    class Meta:
        verbose_name = u'склад'
        verbose_name_plural = u'склады'

    def __unicode__(self):
        return u'{}: расположен в {}'.format(self.name, self.city)

