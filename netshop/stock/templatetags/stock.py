# coding=utf-8
from __future__ import absolute_import
from django import template

register = template.Library()


@register.inclusion_tag('netshop/show_messages.html', takes_context=True)
def show_messages(context, show=True):
    return {
                'messages': (context.get('messages') if show else None)
            }


