# -*- coding: utf-8 -*-
# @Time    : 2018/12/31 0031 15:48
# @Author  : __Yanfeng
# @Site    : 
# @File    : views.py
# @Software: PyCharm
from flask import redirect, render_template, url_for, request
from flask_login import login_required, current_user

from . import admin
from apps.models import User


@admin.route('/')
@login_required
def index():
    return render_template('back/index.html', page_title='Welcome To Blog Server', title='管理员首页')


@admin.route('/users')
@login_required
def users():
    current_page = request.args.get('page', 1, type=int)
    query = User.query.order_by(User.add_time.desc())
    pagination = query.paginate(current_page, per_page=20, error_out=False)
    persons = pagination.items
    return render_template('back/users.html', page_title='用户列表', title='用户列表页', persons=persons, paginations=pagination)


@admin.app_template_test('current_url')
def is_current_url(href):
    return href == request.path
