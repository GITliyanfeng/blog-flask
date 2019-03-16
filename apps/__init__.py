# -*- coding: utf-8 -*-
# @Time    : 2018/12/30 0030 23:29
# @Author  : __Yanfeng
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_pagedown import PageDown
from flask_login import LoginManager

from config import config

BAST_DIR = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
pagedown = PageDown()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'user.user_login'


def create_app(envir):
    app = Flask(__name__)
    app.config.from_object(config[envir])
    db.init_app(app)
    pagedown.init_app(app)
    login_manager.init_app(app)
    from .main import main as main_blueprint
    from .post import post as post_blueprint
    from .user import user as user_blueprint
    from .admin import admin as admin_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(post_blueprint, url_prefix='/post', static_floder='static')
    app.register_blueprint(user_blueprint, url_prefix='/user', static_folder='static')
    app.register_blueprint(admin_blueprint, url_prefix='/admin', static_folder='static')
    app.app_context().push()

    @app.template_filter('md')
    def markdown_to_html(txt):
        from markdown import markdown
        return markdown(txt)

    return app


@login_manager.user_loader
def load_user(userid):
    from apps.models import User
    return User.get_user(userid)
