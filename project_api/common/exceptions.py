#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: exceptions.py
@time: 2017/8/13 下午10:45
"""

from flask_restful import HTTPException

errors = {
    'UNAUTHORIZED': {
        'message': 'Authentication Required.',
        'status': 401,
    },
    'TokenNotExist': {
        'message': 'Token Required.',
        'status': 403,
    },
    'TokenExpired': {
        'message': 'Token Expired.',
        'status': 403,
    },
    'TokenError': {
        'message': 'Token Error.',
        'status': 403,
    },
    'UserAlreadyExistsError': {
        'message': 'A user with that username already exists.',
        'status': 409,
    },
    'ResourceDoesNotExist': {
        'message': 'A resource with that ID no longer exists.',
        'status': 410,
        'extra': 'Any extra information you want.',
    },
}


class UNAUTHORIZED(HTTPException):
    pass


class TokenNotExist(HTTPException):
    pass


class TokenExpired(HTTPException):
    pass


class TokenError(HTTPException):
    pass


class UserAlreadyExistsError(HTTPException):
    pass


class ResourceDoesNotExist(HTTPException):
    pass
