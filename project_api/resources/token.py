#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: token.py
@time: 2017/8/15 上午12:07
"""


from flask import g

from flask_restful import reqparse, abort, Resource

from project_api.common.http_basic_auth import basic_auth

from project_api.common.auth_token import generate_auth_token


class Token(Resource):
    """
    Token
    """
    decorators = [basic_auth.login_required]

    # @basic_auth.login_required
    def get(self):
        """
        get
        Example:
            curl http://0.0.0.0:5000/api/token
            curl -u username:password http://0.0.0.0:5000/api/token
            curl -H "Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=" http://0.0.0.0:5000/api/token
        :return:
        """
        # return g.user_id
        return generate_auth_token(g.user_id)
