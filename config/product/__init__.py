#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: __init__.py.py
@time: 2017/8/14 下午11:00
"""


class ProductConfig(object):
    """
    Production Environment
    """
    DEBUG = False
    SECRET_KEY = '4942e28fe06584fec614693e16a77af7286ba82b8509a999'

    TOKEN_TTL = 600


if __name__ == '__main__':
    import os
    import binascii

    sk = os.urandom(24)
    print sk
    print binascii.b2a_hex(sk)
