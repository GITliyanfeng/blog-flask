# -*- coding: utf-8 -*-
# @Time    : 2019/1/1 0001 20:46
# @Author  : __Yanfeng
# @Site    : 
# @File    : forms.py
# @Software: PyCharm
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, PasswordField, FileField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo


class AddUserForm(FlaskForm):
    choices = [(2, '管理员'), (1, '宾客')]
    username = StringField(label='用户名',
                           validators=[DataRequired(message='不可以为空'), Length(8, 10, message='格式错误,8-10位')])
    email = StringField(label='电子邮箱', validators=[Email(message='电子邮箱格式有误'), DataRequired(message='不可以为空')])
    password = PasswordField(label='密码',
                             validators=[DataRequired(message='不可以为空'), EqualTo('password2', message='两次密码必须一致'),
                                         Regexp('^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,16}$', 0,
                                                message='密码必须为6-16位字母加数字')])
    password2 = PasswordField(label='确认密码', validators=[DataRequired(message='不可以为空')])
    role = SelectField(label='用户类型', coerce=int, choices=choices,
                       render_kw={'data-am-selected': "{searchBox: 1}"})
    face = FileField(label='用户头像', validators=[FileAllowed(['jpg', 'png', 'jpeg'], message='只允许上传图片文件')])
    submit = SubmitField(label='提交')


class LoginForm(FlaskForm):
    username = StringField(label='电子邮箱', validators=[Email(message='电子邮箱格式有误'), DataRequired(message='不可以为空')])
    password = PasswordField(label='密码',validators=[DataRequired(message='不可以为空'),Regexp('^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,16}$', 0,message='密码必须为6-16位字母加数字')])
    submit = SubmitField(label='登陆')
