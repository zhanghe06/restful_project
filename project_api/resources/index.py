#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: index.py
@time: 2017/8/12 下午2:19
"""


from flask_restful import Resource


class Index(Resource):
    """
    Index
    """
    def get(self):
        return {
            'action': self.__class__.__name__,
            'method': 'get'
        }

    def post(self):
        return {
            'action': self.__class__.__name__,
            'method': 'post'
        }
