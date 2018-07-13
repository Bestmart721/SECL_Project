#coding-utf-8

from django.http import  HttpResponse

def main(request, i, j=0):
    return HttpResponse('<h1>Net Shop</h1><p>{}</p><p>{}</p>'.format(i, j))


def post(request, slug):
    return HttpResponse('Post {}'.format(slug))