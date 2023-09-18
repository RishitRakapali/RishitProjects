import wsgiref.simple_server
import urllib.parse
import os
import sys
sys.path.insert(0, '/Users/Rishit/PycharmProjects/BYU_Python/CS_Principles/CSP_Part2/Telephone_Directory')

import databaseModule


def application(environ, start_response):
    headers = [('Content-Type', 'text/plain; charset=utf-8')]

    path = environ['PATH_INFO']
    params = urllib.parse.parse_qs(environ['QUERY_STRING'])

    db = 'httpDB.txt'

    if path == '/insert':
        databaseModule.insert(db, params['key'][0], params['value'][0])
        start_response('200 OK', headers)
        return ['Inserted'.encode()]
    elif path == '/select':
        s = databaseModule.select_one(db, params['key'][0])
        start_response('200 OK', headers)
        if s:
            return [s.encode()]
        else:
            return ['NULL'.encode()]
    elif path == '/delete':
        s = databaseModule.select_one(db, params['key'][0])
        start_response('200 OK', headers)
        if s:
            databaseModule.delete(db, params['key'][0])
            return ['Deleted'.encode()]
        else:
            return ['NULL'.encode()]
    elif path == '/update':
        s = databaseModule.select_one(db, params['key'][0])
        start_response('200 OK', headers)
        if s:
            databaseModule.update(db, params['key'][0], params['value'][0])
            return ['Updated'.encode()]
        else:
            return ['NULL'.encode()]
    else:
        start_response('404 Not Found', headers)
        return ['Status 404: Resource not found'.encode()]


httpd = wsgiref.simple_server.make_server('', 8000, application)
httpd.serve_forever()