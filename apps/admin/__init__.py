# -*- coding: utf-8 -*-
# @Time    : 2018/12/31 0031 15:09
# @Author  : __Yanfeng
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Blueprint

admin = Blueprint('admin', __name__)
from . import views
