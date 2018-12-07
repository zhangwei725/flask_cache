from flask import Flask

# 程序的入口
from apps.ext import init_ext
from apps.mian.views import main
from upfile.views import upload


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '123456789'
    app.debug = True
    register(app)
    init_ext(app)
    return app


def register(app: Flask):
    app.register_blueprint(main)
    app.register_blueprint(upload)
