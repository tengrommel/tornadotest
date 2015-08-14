#!/usr/bin/env python
# coding=utf-8
__author__ = 'teng'


import MySQLdb
conn = MySQLdb.connect(host="localhost", user="root", passwd="teng", db="tengtest", port=3306, charset="utf8")

cur = conn.cursor()     # 游标对象