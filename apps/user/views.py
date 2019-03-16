# -*- coding: utf-8 -*-
# @Time    : 2018/12/31 0031 15:48
# @Author  : __Yanfeng
# @Site    : 
# @File    : views.py
# @Software: PyCharm
import os
import time

from flask import redirect, render_template, url_for, request
from werkzeug.utils import secure_filename
from flask_login import logout_user, login_user, current_user, login_required

from . import user
from .forms import AddUserForm, LoginForm
from apps import BAST_DIR, db
from apps.models import User


@user.route('/user', methods=['GET', 'POST'])
@login_required
def adduser():
    form = AddUserForm()
    form.role.data = 1
    if form.validate_on_submit():
        file = request.files.get('face', '')
        file_name, file_path = upload_file(file, username=form.username.data)
        person = User()
        person.username = form.username.data
        person.password = form.password.data
        person.email = form.email.data
        person.face = file_name
        person.face_path = file_path
        person.role_id = form.role.data
        db.session.add(person)
        db.session.commit()
        return redirect(url_for('admin.users'))
    return render_template('back/user.html', page_title='增加用户', title='增加用户页', form=form)


@login_required
def upload_file(file, username=None):
    if username:
        username = username
    else:
        username = 'test'
    file = file
    if file:
        basedir = BAST_DIR
        upload_path = os.path.join(basedir, 'static/user/user_face')
        file_name = secure_filename(file.filename)
        file_type = file_name.rsplit('.').pop()
        file_name = str(username) + '_' + str(time.strftime("%Y_%m_%d__%H_%M_%S", time.localtime())) + '.' + file_type
        file_path = os.path.join(upload_path, file_name).replace('\\', '/')
        file.save(file_path)
        res = ('user/user_face/{file_name}'.format(file_name=file_name), file_path)
        return res
    res = ('user/user_face/default.jpg', None)
    return res


@user.route('/login', methods=['POST', 'GET'])
def user_login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.username.data
        password = form.password.data
        user = User.query.filter_by(email=email, password=password).first()
        if not user:
            form.username.errors.insert(0, '用户名或者密码错误')
        else:
            login_user(user=user)
            return redirect(url_for('admin.index'))
    return render_template('back/login.html', form=form)


@user.route('/logout')
@login_required
def user_logout():
    logout_user()
    return redirect(url_for('user.user_login'))


@user.app_template_test('current_url')
def is_current_url(href):
    return href == request.path
