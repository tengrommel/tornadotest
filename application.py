#!/usr/bin/env python
# coding=utf-8

__author__ = 'teng'

# from url import url是将url.py中设定的目录引用过来。
from url import url
import base64
import uuid
import tornado.web
import os

# setting引用了一个字典对象，里面约定了模板和静态文件的路径，
# 即声明已经建立的文件夹"templates"和"statics"分别为模板目录和静态文件目录。
# 随机获取一个地址
cookiefor = base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "statics"),
    cookie_secret=cookiefor,
    xsrf_cookies=True,
    # ，如果用户不合法，根据这个设置，会返回到首页
    login_url='/',
    debug=True
)


# 接下来的application就是一个请求处理集合对象。请注意tornado.web.Application()的参数设置：
# tornado.web.Application(handlers=None, default_host='', transforms=None, **settings)

application = tornado.web.Application(
    handlers=url,
    **settings
)


