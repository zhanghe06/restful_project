#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: index.py
@time: 2017/8/12 下午2:19
"""


from flask_restful import reqparse, abort, Resource


USERS = {
    'user1': {'task': 'create flask restful project'},
    'user2': {'task': 'deploy flask restful project'},
    'user3': {'task': 'reload flask restful project'},
    # 'user3': {'task': 'review flask restful project'},
    # 'user4': {'task': 'revise flask restful project'},
}


def abort_if_user_doesnt_exist(user_id):
    if user_id not in USERS:
        abort(404, message="User {} doesn't exist".format(user_id))

parser = reqparse.RequestParser()
parser.add_argument('task', required=True, help="Task cannot be blank!")


class User(Resource):
    """
    User
    """
    def get(self, user_id):
        """
        get
        Example:
            curl http://0.0.0.0:5000/api/user/1
            {
                "task": "create flask restful project"
            }
        :param user_id:
        :return:
        """
        user_id = 'user%i' % user_id
        abort_if_user_doesnt_exist(user_id)
        return USERS[user_id]

    def delete(self, user_id):
        """
        delete
        Example:
            curl http://0.0.0.0:5000/api/user/1 -X DELETE
        :param user_id:
        :return:
        """
        user_id = 'user%i' % user_id
        abort_if_user_doesnt_exist(user_id)
        del USERS[user_id]
        return '', 204

    def put(self, user_id):
        """
        put
        Example:
            curl http://0.0.0.0:5000/api/user/3 -d "task=review flask restful project" -X PUT
            {
                "task": "review flask restful project"
            }
        :param user_id:
        :return:
        """
        args = parser.parse_args()
        user_id = 'user%i' % user_id
        task = {'task': args['task']}
        USERS[user_id] = task
        return task, 201


class UserList(Resource):
    """
    UserList
    """
    def get(self):
        """
        get
        Example:
            curl http://0.0.0.0:5000/api/user_list
            {
                "user1": {
                    "task": "create flask restful project"
                },
                "user2": {
                    "task": "deploy flask restful project"
                },
                "user3": {
                    "task": "reload flask restful project"
                }
            }
        :return:
        """
        return USERS

    def post(self):
        """
        post
        Example:
            curl http://0.0.0.0:5000/api/user_list -d "task=revise flask restful project" -X POST
            {
                "task": "revise flask restful project"
            }
        :return:
        """
        args = parser.parse_args()
        user_id = int(max(USERS.keys()).lstrip('user')) + 1
        print user_id
        user_id = 'user%i' % user_id
        USERS[user_id] = {'task': args['task']}
        return USERS[user_id], 201
