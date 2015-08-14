#!/usr/bin/env python
# coding=utf-8
__author__ = 'teng'

import tornado.escape
import sys
sys.path.append(r'..')
import methods.readdb as mrd
from base import BaseHandler
class IndexHandler(BaseHandler):
    def get(self):
        username = mrd.select_columns(table="users", column="username")
        one_user = username[0][0]
        # 其中user=one_user的作用就是传递对象到模板
        self.render("index.html", user=one_user)

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
# 在post()方法中，使用get_argument()函数来接收前端传过来的数据，
# 这个函数的完整格式是get_argument(name, default=[], strip=True)，
# 它能够获取name的值。在上面的代码中，name就是从前端传到后端的那个json
# 对象的键的名字，是哪个键就获取该键的值。如果获取不到name的值，就返回
# default的值，但是这个值默认是没有的，如果真的没有就会抛出HTTP 400。
# 特别注意，在get的时候，通过get_argument()函数获得url的参数，
# 如果是多个参数，就获取最后一个的值。要想获取多个值，
# 可以使用get_arguments(name, strip=true)。
# 在设置setting的时候，写上debug = True就表示是调试模式了（参阅：用tornado做网站(1)）。
# 但是，调试模式也不是十全十美，如果修改模板，就不会加载，还需要重启服务
        user_infos = mrd.select_table(table="users", column="*", condition="username", value=username)
        if user_infos:
            db_pwd = user_infos[0][2]
            if db_pwd == password:
                self.set_current_user(username)
                self.write(username)
            else:
                self.write("-1")
        else:
            self.write("-1")


    def set_current_user(self, user):
        if user:
            self.set_secure_cookie('user', tornado.escape.json_encode(user))    #注意这里使用了tornado.escape.json_encode()方法
        else:
            self.clear_cookie("user")

class ErrorHandler(BaseHandler):    #增加了一个专门用来显示错误的页面
    def get(self):                                        #但是后面不单独讲述，读者可以从源码中理解
        self.render("error.html")
