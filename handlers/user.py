#!/usr/bin/env python
# coding=utf-8
__author__ = 'teng'
import tornado.escape
import tornado.web
import sys
sys.path.append(r'..')
from base import BaseHandler
import methods.readdb as mrd

class UserHandler(BaseHandler):
    # 作用就是完成tornado的认证功能
    @tornado.web.authenticated
    def get(self):
        # escape
        #username = tornado.escape.json_decode(self.current_user)
        #username = self.get_argument("user")
        # users = username.split(' ')
        # print users[2]
        username = tornado.escape.json_decode(self.current_user)
        user_infos = mrd.select_table(table="users",column="*",condition="username",value=username)
        self.render("user.html", users = user_infos)
# get()使用self.get_argument("user")，目的是要通过url的值。
# 因此，当用户登录后，得到正确返回值js应该用这样的方式载入新的页面。
