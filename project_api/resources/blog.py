#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: blog.py
@time: 2017/8/13 下午11:25
"""


from flask_restful import reqparse, abort, Resource

from project_api.common.http_auth import auth
from project_api.common.exceptions import ResourceDoesNotExist


BLOGS = {
    'blog1': {'author': 'beta', 'title': 'blog title', 'done': True},
}


class Blog(Resource):
    """
    Blog
    """
    decorators = [auth.login_required]

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
            curl -u username:password http://0.0.0.0:5000/api/blog/1
        :param blog_id:
        :return:
        """
        blog_id = 'blog%i' % blog_id
        if blog_id not in BLOGS:
            raise ResourceDoesNotExist()
        return BLOGS[blog_id]
