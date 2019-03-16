# -*- coding: utf-8 -*-
# @Time    : 2018/12/30 0030 23:53
# @Author  : __Yanfeng
# @Site    : 
# @File    : config.py
# @Software: PyCharm


class Config(object):
    SECRET_KEY = 'a simple string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECODE_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    def __init__(self):
        pass


class DervelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@127.0.0.1:3306/database'


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@127.0.0.1:3306/database'


config = {
    'dervelopnemnt': DervelopmentConfig,
    'production': ProductionConfig,
}
