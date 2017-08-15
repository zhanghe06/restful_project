#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: blog.py
@time: 2017/8/13 下午11:25
"""


from flask_restful import reqparse, abort, Resource

from project_api.common.http_token_auth import token_auth
from project_api.common.exceptions import ResourceDoesNotExist


BLOGS = {
    'blog1': {'author': 'beta', 'title': 'blog title', 'done': True},
}


class Blog(Resource):
    """
    Blog
    """
    decorators = [token_auth.login_required]

    def __init__(self):
        self.parse = reqparse.RequestParser()
        self.parse.add_argument('author', type=str, location='json')
        self.parse.add_argument('title', type=str, location='json')
        self.parse.add_argument('done', type=bool, location='json')
        super(Blog, self).__init__()

    def get(self, blog_id):
        """
        get
        Example:
            curl http://0.0.0.0:5000/api/blog/1
            curl http://0.0.0.0:5000/api/blog/1 -H "Authorization: Token eyJhbGciOiJIUzI1NiIsImV4cCI6MTUwMjc3NTg4OSwiaWF0IjoxNTAyNzc1Mjg5fQ.eyJ1c2VyX2lkIjoxfQ.Z4G_vjLzkV_alxXBPfxa0H4Kh5gC4PD5LA-iqNynB7o"
            curl http://0.0.0.0:5000/api/blog/1 --oauth2-bearer eyJhbGciOiJIUzI1NiIsImV4cCI6MTUwMjc3NTg4OSwiaWF0IjoxNTAyNzc1Mjg5fQ.eyJ1c2VyX2lkIjoxfQ.Z4G_vjLzkV_alxXBPfxa0H4Kh5gC4PD5LA-iqNynB7o
        :param blog_id:
        :return:
        """
        blog_id = 'blog%i' % blog_id
        if blog_id not in BLOGS:
            raise ResourceDoesNotExist()
        return BLOGS[blog_id]
