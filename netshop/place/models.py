# coding=utf-8
from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=60, verbose_name=u'название')

    class Meta:
        verbose_name = u'страна'
        verbose_name_plural = u'страны'

    def __unicode__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=60, verbose_name=u'название')
    country = models.ForeignKey('Country')

    class Meta:
        verbose_name = u'город'
        verbose_name_plural = u'города'

    def __unicode__(self):
        return u'город: {} ({})'.format(self.name, self.country)