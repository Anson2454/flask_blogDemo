import os
from redis import Redis


class BaseConfig(object):
    SESSION_TYPE = "redis"
    SESSION_REDIS = Redis(host="127.0.0.1", port=6379)

    # #### SECRET #####
    SECRET_KEY = 'dev'

    # ##### SQLAlchemy 相关配置 #####
    SQLALCHEMY_DATABASE_URI = os.getenv('LOCAL_DB')  # 从本地环境变量读取数据库配置 连接数据库
    SQLALCHEMY_POOL_SIZE = 10  # 连接池大小
    SQLALCHEMY_MAX_OVERFLOW = 5  # 连接池 最大溢出
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    pass


class ProConfig(BaseConfig):
    pass
