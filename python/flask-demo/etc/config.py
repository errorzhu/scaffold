import os

current_dir = os.path.dirname(__file__)
basedir = os.path.abspath(os.path.join(current_dir, "../../"))


class Config:
    SECRET_KEY = 'the quick brown fox jumps over the lazy dog'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    def init_app(app):
        pass


class DevelopmentConfig(Config):
    HOST = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'flask'
    USERNAME = 'root'
    PASSWORD = '123456'
    DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8" \
        .format(username=USERNAME,
                password=PASSWORD,
                host=HOST,
                port=PORT,
                db=DATABASE)
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = DB_URI


class TestingConfig(Config):
    TESTING = True
    HOST = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'flask_test'
    USERNAME = 'root'
    PASSWORD = '123456'
    DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8" \
        .format(username=USERNAME,
                password=PASSWORD,
                host=HOST,
                port=PORT,
                db=DATABASE)
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = DB_URI


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
