#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: app.py
@time: 2017/8/12 下午12:22
"""


from flask import Flask, Blueprint
from flask_restful import Api

from config import current_config
from project_api.resources.index import Index
from project_api.resources.token import Token
from project_api.resources.user import User
from project_api.resources.user import UserList
from project_api.resources.role import Role
from project_api.resources.role import RoleList
from project_api.resources.blog import Blog

from project_api.common.exceptions import errors


app = Flask(__name__)

# Load Config
app.config.from_object(current_config)

api_bp = Blueprint('api', __name__, url_prefix='/api')

api = Api(api_bp, errors=errors)

# Add Resource
api.add_resource(Index, '/', '/index', endpoint='index')
api.add_resource(Token, '/token', endpoint='token')
api.add_resource(User, '/user/<int:user_id>', endpoint='user')
api.add_resource(UserList, '/user_list', endpoint='user_list')
api.add_resource(Role, '/role/<int:role_id>', endpoint='role')
api.add_resource(RoleList, '/role_list', endpoint='role_list')
api.add_resource(Blog, '/blog/<int:blog_id>', endpoint='blog')

app.register_blueprint(api_bp)
