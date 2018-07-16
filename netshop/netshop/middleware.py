# -*- coding: utf-8 -*-
from __future__ import absolute_import
import datetime

List = []
class MyMiddleware(object):
    """My middleware that collect data from requests and write it
    into the file requests.log"""
    def process_request(self, request):
        """Updating global list with requests"""
        global List
        timer = 'Request: {}'.format(datetime.datetime.now())
        my_logs = (timer, request.method, request.build_absolute_uri())
        List.append(my_logs)


    def process_response(self, request, response):
        global List
        timer = '(\'Response: {}\')'.format(datetime.datetime.now())
        List.append(timer)
        if request:
            with open('requests.log', 'w') as f:
                for t in List:
                    f.write('{}\n'.format(t))
        return response

