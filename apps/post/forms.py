# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 0002 12:47
# @Author  : __Yanfeng
# @Site    : 
# @File    : forms.py
# @Software: PyCharm
from flask_wtf import FlaskForm
from flask_pagedown.fields import PageDownField
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField(label='标题', validators=[DataRequired(message='标题内容不可为空'), ])
    desc = TextAreaField(label='简述', validators=[DataRequired(message='简述内容不可为空'), ])
    body = PageDownField(label='内容', validators=[DataRequired(message='主要内容不可为空')])
    submit = SubmitField(label='提交')
