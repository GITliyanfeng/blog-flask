# -*- coding: utf-8 -*-
# @Time    : 2018/12/30 0030 23:29
# @Author  : __Yanfeng
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Blueprint

user = Blueprint('user', __name__)

from . import views, forms
