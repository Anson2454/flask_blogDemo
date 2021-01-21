from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_session import session

# 实例化SQLAlchemy
db = SQLAlchemy()  # db 这个对象中含有 SQLAlchemy 需要的所有东西，唯独少 数据库连接
# 注意： SQLAlchemy 的实例化必须要在 蓝图的上面


from .models import *


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    # manager = Manager(app)
    app.debug = True

    # 配置项可以单独管理
    app.config.from_object("config.ProConfig")

    # 注册auth 蓝图
    from .views.auth import bp as a_bp
    app.register_blueprint(a_bp)
    # 注册blog 蓝图
    from .views.blog import bp as b_bp
    app.register_blueprint(b_bp)
    app.add_url_rule('/', endpoint='index')

    # 初始化SQLAlchemy
    db.init_app(app)
    return app
