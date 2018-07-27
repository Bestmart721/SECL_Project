# coding=utf-8
from __future__ import absolute_import
from django import template

register = template.Library()


def my_sort(value):
    list1 = str(value).split(' ')
    list1.sort(key=lambda x:x[0])
    new_list = []
    while len(list1) != 0:
        new_list.append(list1[0] + ' ' + list1[1])
        del list1[0:2]
    new_list.sort(key=lambda x:x[0])
    for i in new_list:
        return i


register.filter('my_sort', my_sort)
