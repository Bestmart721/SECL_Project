# coding=utf-8

from django.db import models

# class CustomManager(models.Manager):
#     def get_queryset(self):
#         return super(CustomManager, self).get_queryset().filter(gender=Person.FEMALE)
#

# Create your models here.
class Person(models.Model):
    MALE = 0
    FEMALE = 1
    GENDER_CHOICES = (
        (MALE, u'мужской'),#зліва, те що зберігається в бд, зправа хтмл
        (FEMALE, u'женский'),
    )
    first_name = models.CharField(max_length=48, verbose_name=u'имя')
    last_name = models.CharField(max_length=58, verbose_name=u'фамилия')
    gender = models.CharField(max_length=8, choices=GENDER_CHOICES, verbose_name=u'пол', null=True, blank=True)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, verbose_name=u'дата рождения')
    email = models.EmailField(max_length=254, unique=True, verbose_name=u'электронный адрес')

    # males = CustomManager()
    # object = models.Manager()

    class Meta:
        verbose_name = u'контактное лицо'
        verbose_name_plural = u'контактние лица'

    def __unicode__(self):
        return u'{} {}'.format(self.first_name, self.last_name)