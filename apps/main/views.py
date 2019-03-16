# -*- coding: utf-8 -*-
# @Time    : 2018/12/31 0031 0:12
# @Author  : __Yanfeng
# @Site    : 
# @File    : views.py
# @Software: PyCharm
from functools import reduce

from flask import redirect, render_template, request
from os import path

from . import main
from apps import BAST_DIR
from apps.models import Post, Archive


@main.route('/')
def index():
    current_page = request.args.get('page', 1, type=int)
    query = Post.query.order_by(Post.add_time.desc())
    pagination = query.paginate(current_page, per_page=20, error_out=False)
    posts = pagination.items
    return render_template('front/index.html', title='博客首页', posts=posts, paginations=pagination)


@main.route('/adout')
def about():
    return render_template('front/about.html', title='关于我')


@main.route('/archive')
def archive():
    all_group = Archive.query.order_by(Archive.name.desc()).all()
    return render_template('front/archive.html', title='归档', all_group=all_group)


@main.route('/links')
def links():
    return render_template('front/link.html', title='友链')


@main.app_template_test('current_url')
def is_current_url(href):
    return href == request.path


def read_md(filename):
    filename = path.join(BAST_DIR, filename)
    with open(filename, encoding='utf-8') as md_f:
        content = reduce(lambda x, y: x + y, md_f.readlines())
    return content


@main.context_processor
def inject_methods():
    return dict(read_md=read_md)
