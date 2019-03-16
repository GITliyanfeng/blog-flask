# -*- coding: utf-8 -*-
# @Time    : 2018/12/31 0031 0:04
# @Author  : __Yanfeng
# @Site    : 
# @File    : manager.py
# @Software: PyCharm
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand, upgrade
from apps import create_app, db
from apps.models import User, Role

app = create_app('production')
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    pass


@manager.command
def deploy():
    upgrade()
    Role.seed()


@manager.command
def forged():
    from forgery_py import basic, lorem_ipsum, name, internet, date
    from random import randint
    db.drop_all()
    db.create_all()
    Role.seed()
    guests = Role.query.first()

    def generate_user():
        from apps.models import User
        user = User()
        user.username = internet.user_name()
        user.email = internet.email_address()
        user.password = basic.text(8, at_least=8, spaces=False)
        user.role = guests
        return user

    def generate_post(func_author):
        from apps.models import Post
        post = Post()
        post.title = lorem_ipsum.title()
        post.body = lorem_ipsum.paragraph()
        post.desc = lorem_ipsum.paragraph()
        time_ = date.date(past=True)
        post.add_time = time_
        post.add_year = time_.year
        post.author = func_author()
        return post

    users = [generate_user() for i in range(0, 5)]
    db.session.add_all(users)
    random_user = lambda: users[randint(0, 4)]
    posts = [generate_post(random_user) for i in range(0, randint(60, 200))]
    db.session.add_all(posts)
    db.session.commit()
    print('Done!!!!')


@manager.command
def createsuperuser():
    while True:
        username = input('请输入用户名:')
        email = input('请输入电子邮箱:')
        password = input('请输入密码:')
        password2 = input('确认密码:')
        if password != password2:
            continue
        user = User()
        user.username = username
        user.password = password
        user.role_id = 2
        user.email = email
        db.session.add(user)
        db.session.commit()
        print('createsupersuer  success!!!')
        break


if __name__ == '__main__':
    manager.run()
