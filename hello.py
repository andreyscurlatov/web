#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     18.06.2020
# Copyright:   (c) User 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

def app(env, start_response):

    data = [bytes(i + "\n", 'utf-8') for i in env['QUERY_STRING'].split('&')]

    status = '200 OK'

    headers = [('Content-Type', 'text/plain'),]

    start_response(status, headers)

    return data





