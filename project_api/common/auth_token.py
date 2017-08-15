#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: auth_token.py
@time: 2017/8/14 下午10:42
"""

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired, BadSignature

from project_api.common.exceptions import TokenError, TokenExpired, TokenNotExist


def generate_auth_token(user_id):
    from project_api.app import app
    s = Serializer(app.config['SECRET_KEY'], expires_in=app.config['TOKEN_TTL'])
    return s.dumps({'user_id': user_id})


def verify_auth_token(token):
    if not token:
        raise TokenNotExist
    from project_api.app import app
    s = Serializer(app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
        return data
    except SignatureExpired:
        raise TokenExpired
        # return None  # valid token, but expired
    except BadSignature:
        raise TokenError
        # return None  # invalid token
    # user = User.query.get(data['id'])
    # return user
    # return {'user_id': 1, 'user_name': 'tom'}
