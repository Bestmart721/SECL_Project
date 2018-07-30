# coding=utf-8
from __future__ import absolute_import
import datetime
from django import template
from person.models import Person

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



# @register.filter(expects_localtime=True)
# def test(value):
#     return value
#
# @register.simple_tag(takes_context=True)
# def current_time(context, f, prefix=None):
#     prefix = prefix or context.get('date_prefix', '')
#     context['t'] = Person.objects.get(pk=1)
#     return prefix + datetime.datetime.now().strftime(f)
#
# @register.inclusion_tag('shop/menu.html', takes_context=True)
# def menu(context, selected=None):
#     return {
#         'items': ['Menu 1', 'Menu 2', 'Menu 3'],
#         'selected': selected or context.get('selected_menu')
#     }
@register.inclusion_tag('shop/show_messages.html', takes_context=True)
def show_messages(context, message=True):
    return {
        'messages': (context.get('messages') if message else None)}


