#!/usr/bin/env python
# coding=utf-8
__author__ = 'teng'
"""
the url structure of website
"""

import sys  # utf-8 兼容汉字
reload(sys)
sys.setdefaultencoding("utf-8")

# url.py文件主要是设置网站的目录结构。
# from handlers.index import IndexHandler，
# 虽然在handlers文件夹还没有什么东西，为了演示如何建立网站的目录结构，
# 假设在handlers文件夹里面已经有了一个文件index.py，它里面还有一个类IndexHandler。
# 在url.py文件中，将其引用过来。

from handlers.index import IndexHandler
from handlers.user import UserHandler

url = [
    (r'/', IndexHandler),
    (r'/user', UserHandler)
]
# 变量url指向一个列表，在列表中列出所有目录的对应的处理类。
# 比如(r'/', IndexHandler)，就是约定网站根目录的处理类
# 是IndexHandler，即来自这个目录的get()或者post()请求，
# 均有IndexHandler类中相应方法来处理。

