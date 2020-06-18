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

from urllib.parse import parse_qs

def app(env, start_response):

    d = {}

    d = parse_qs(env['QUERY_STRING'])

    l = []

    for key in d:
        l.append("%s=%s" % (key, d[key]))

    status = '200 OK'

    headers = [('Content-Type', 'text/plain'),]

    start_response(status, headers)

    return l



