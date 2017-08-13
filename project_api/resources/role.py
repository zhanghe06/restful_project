#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: role.py
@time: 2017/8/12 下午5:06
"""


from flask_restful import reqparse, abort, Resource


ROLES = {
    'role1': {'name': 'admin', 'modules': 'index, user, order, stats'},
    'role2': {'name': 'guest', 'modules': 'index'},
    # 'role2': {'name': 'junior', 'modules': 'index, user'},
    # 'role3': {'name': 'senior', 'modules': 'index, user, order'},
}


def abort_if_role_doesnt_exist(role_id):
    if role_id not in ROLES:
        abort(404, message="Role {} doesn't exist".format(role_id))

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('modules')


class Role(Resource):
    """
    Role
    """
    def get(self, role_id):
        """
        get
        Example:
            curl http://0.0.0.0:5000/api/role/1
            {
                "modules": "index, user, order, stats",
                "name": "admin"
            }
        :param role_id:
        :return:
        """
        role_id = 'role%i' % role_id
        abort_if_role_doesnt_exist(role_id)
        return ROLES[role_id]

    def delete(self, role_id):
        """
        delete
        Example:
            curl http://0.0.0.0:5000/api/role/1 -X DELETE
        :param role_id:
        :return:
        """
        role_id = 'role%i' % role_id
        abort_if_role_doesnt_exist(role_id)
        del ROLES[role_id]
        return '', 204

    def put(self, role_id):
        """
        put
        Example:
            curl http://0.0.0.0:5000/api/role/2 -d "name=junior" -d "modules=index, user" -X PUT
            {
                "modules": "index, user",
                "name": "junior"
            }
        :param role_id:
        :return:
        """
        args = parser.parse_args()
        role_id = 'role%i' % role_id
        info = {
            'name': args['name'],
            'modules': args['modules']
        }
        ROLES[role_id] = info
        return info, 201


class RoleList(Resource):
    """
    RoleList
    """
    def get(self):
        """
        get
        Example:
            curl http://0.0.0.0:5000/api/role_list
            {
                "role1": {
                    "modules": "index, user, order, stats",
                    "name": "admin"
                },
                "role2": {
                    "modules": "index, user",
                    "name": "junior"
                }
            }
        :return:
        """
        return ROLES

    def post(self):
        """
        post
        Example:
            curl http://0.0.0.0:5000/api/role_list -d "name=senior" -d "modules=index, user, order" -X POST
            {
                "modules": "index, user, order",
                "name": "senior"
            }
        :return:
        """
        args = parser.parse_args()
        role_id = int(max(ROLES.keys()).lstrip('role')) + 1
        print role_id
        role_id = 'role%i' % role_id
        ROLES[role_id] = {
            'name': args['name'],
            'modules': args['modules']
        }
        return ROLES[role_id], 201
