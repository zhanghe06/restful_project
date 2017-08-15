#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: __init__.py.py
@time: 2017/8/14 下午11:00
"""


class DevelopConfig(object):
    """
    Development Environment
    """
    DEBUG = True
    SECRET_KEY = '876de9c54eca3989e4115c1cec711243d16f7c2d95976bab'

    TOKEN_TTL = 600


if __name__ == '__main__':
    import os
    import binascii

    sk = os.urandom(24)
    print sk
    print binascii.b2a_hex(sk)
