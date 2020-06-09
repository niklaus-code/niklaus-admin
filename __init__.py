# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.fileadmin import FileAdmin
import os.path as op


app = Flask(__name__, template_folder='templates')
db = SQLAlchemy(app)

 
#from .view import Login, MyblogModel, ArticleCategoryModel, TopArticleModel, UsPramaModel, MyblogReadModel
from .view import Login, MyblogModel, ArticleCategoryModel, TopArticleModel, UsPramaModel, MyblogReadModel, ThoughtsModel
from .model import Myblog_read, Myblog_list, Article_class, Top_list, Us_prama, Myblog_thoughts
#from .model import Myblog_read, Myblog_list, Article_class, Top_list, Us_prama


def create_app():
    admin = Admin(app, name='MyAdmin', index_view=AdminIndexView(template='home.html'), template_mode='bootstrap3')

    app.config['SECRET_KEY'] = '123456'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ysman:123456@127.0.0.1:3306/myblog?charset=utf8mb4'

    admin.add_view(MyblogModel(Myblog_list, db.session))
    admin.add_view(ArticleCategoryModel(Article_class, db.session))
    #admin.add_view(TopArticleModel(Top_list, db.session))
    #admin.add_view(UsPramaModel(Us_prama, db.session))
    admin.add_view(MyblogReadModel(Myblog_read, db.session))
    admin.add_view(ThoughtsModel(Myblog_thoughts, db.session))

    path = op.join(op.dirname(__file__), '/var/www/ivue-master/static')
    admin.add_view(FileAdmin(path, '/img', name='Static Files'))

    return app
