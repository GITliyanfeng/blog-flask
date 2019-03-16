# -*- coding: utf-8 -*-
# @Time    : 2018/12/31 0031 0:28
# @Author  : __Yanfeng
# @Site    : 
# @File    : models.py
# @Software: PyCharm
from datetime import datetime
from markdown import markdown
from flask_login import UserMixin

from . import db


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=True)
    users = db.relationship('User', backref='role')

    @staticmethod
    def seed():
        db.session.add_all(map(lambda r: Role(name=r), ['Guests', 'Admin']))
        db.session.commit()


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=True)
    password = db.Column(db.String(100), nullable=True)
    face = db.Column(db.String(100), nullable=True)
    face_path = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    posts = db.relationship('Post', backref='author')
    add_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    @staticmethod
    def on_create(target, value, oldvalue, initiator):
        target.role = Role.query.filter_by(name='Guests').first()

    @staticmethod
    def get_user(userid):
        userid = int(userid)
        user = User.query.filter_by(id=userid).first()
        return user


# db.event.listen(User.username, 'set', User.on_create)

class Archive(db.Model):
    __tablename__ = 'archives'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, index=True, nullable=True)
    posts = db.relationship('Post', backref='arc')

    def get_order_item(self):
        items = self.posts.order_by(Post.add_time.desc())
        return items


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=True)
    desc = db.Column(db.Text)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    arc_id = db.Column(db.Integer, db.ForeignKey('archives.id'))
    add_year = db.Column(db.String(40), default=datetime.now().year)
    add_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    __mapper_args__ = {'order_by': add_time.desc()}

    @staticmethod
    def check_admin(user):
        return user.role.name == 'Admin'

    @staticmethod
    def on_body_change(target, value, oldvalue, initiator):
        if value is None or (value == ''):
            target.body_html = ''
        else:
            target.body_html = markdown(value)

    @staticmethod
    def on_addyeay_change(target, value, oldvalue, initiator):
        name = value
        obj = Archive.query.filter_by(name=name).first()
        if not obj:
            Arc = Archive(name=name)
            db.session.add(Arc)
            db.session.commit()
            target.arc = Arc
        else:
            target.arc = obj


db.event.listen(Post.body, 'set', Post.on_body_change)
db.event.listen(Post.add_year, 'set', Post.on_addyeay_change)
