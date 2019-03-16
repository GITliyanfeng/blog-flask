# -*- coding: utf-8 -*-
# @Time    : 2019/1/5 0005 21:53
# @Author  : __Yanfeng
# @Site    : 
# @File    : uwsgi.py
# @Software: PyCharm

from apps import create_app

application = create_app(envir='production')

if __name__ == '__main__':
    application.run()
