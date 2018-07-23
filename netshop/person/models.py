# coding=utf-8
from django.db import models


class Person(models.Model):
    """The model of person
    special: choices of gender
    additional methodes fullname and description"""
    MALE = 0
    FEMALE = 1
    GENDER_CHOICES = (
        (MALE, u'мужской'),
        (FEMALE, u'женский'),
    )
    first_name = models.CharField(max_length=48, verbose_name=u'имя')
    last_name = models.CharField(max_length=58, verbose_name=u'фамилия')
    gender = models.CharField(max_length=8, choices=GENDER_CHOICES, verbose_name=u'пол', null=True, blank=True)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, verbose_name=u'дата рождения')
    email = models.EmailField(max_length=254, unique=True, verbose_name=u'электронный адрес')

    class Meta:
        verbose_name = u'контактное лицо'
        verbose_name_plural = u'контактние лица'

    def __unicode__(self):
        return u'{} {}'.format(self.first_name, self.last_name)

    def fullname(self):
        return self.first_name + ' ' + self.last_name

    def description(self):
        return u'{} - пол: {}, дата рождения: {}, электронный адрес: {}'.format(self.fullname(), self.get_gender_display(), self.date_of_birth, self.email)

    @models.permalink
    def get_absolute_url(self):
        return 'person_detail', (), {'pk': self.pk}