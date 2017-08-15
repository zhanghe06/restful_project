#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: __init__.py.py
@time: 2017/8/14 下午10:59
"""


import os

from config.product import ProductConfig
from config.develop import DevelopConfig


class DefaultConfig(object):
    pass


config_map = {
    'default': DefaultConfig,
    'develop': DevelopConfig,
    'product': ProductConfig,
}

current_config = config_map.get(os.environ.get('MODE'), DefaultConfig)
