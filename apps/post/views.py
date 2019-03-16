# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 0002 12:47
# @Author  : __Yanfeng
# @Site    : 
# @File    : views.py
# @Software: PyCharm
from flask import redirect, render_template, url_for, request
from flask_login import login_required,current_user

from . import post
from .forms import PostForm
from apps.models import Post, db, User


@post.route('/posts')
@login_required
def posts():

    current_page = request.args.get('page', 1, type=int)
    query = Post.query.order_by(Post.add_time.desc())
    pagination = query.paginate(current_page, per_page=20, error_out=False)
    post = pagination.items
    return render_template('back/posts.html', title='博文列表', page_title='欢迎来到博文列表', post=post, paginations=pagination)


@post.route('/post', methods=['POST', 'GET'])
@login_required
def post_():
    form = PostForm()
    if form.validate_on_submit():
        my_post = Post()
        my_post.title = form.title.data
        my_post.body = form.body.data
        my_post.desc = form.desc.data
        my_post.author_id = 2
        db.session.add(my_post)
        db.session.commit()
        return redirect(url_for('post.posts'))

    return render_template('back/post.html', title='添加博文', page_title='添加博文', form=form)


@post.route('/detail/<int:post_id>', methods=['POST', 'GET'])
def details(post_id):
    post = Post.query.get_or_404(int(post_id))
    return render_template('front/detaile.html', title=post.title, post=post)



