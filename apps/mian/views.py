import datetime
import random

from flask import Blueprint, render_template

from apps.config import BlueKeyConfig
from apps.ext import cache

main = Blueprint(BlueKeyConfig.BLUEPRINT_MAIN_KEY, __name__)

# 注意 缓存装饰器尽量写在蓝图的下面
"""
timeout 单位是秒 none 默认永不过期
# redis 雪崩 产生的主要原因是同一时刻大量的数据同时过期
            在设置缓存的时间上加上随机数
"""


@main.route('/')
@cache.cached(timeout=20 + random.randint(10, 60), key_prefix='view_index')
def index():
    return render_template('index.html', now=datetime.datetime.now())


"""
cached  不支持视图函数带参数
memoize 支持视图函数带参数
"""


# 设置缓存key的名称
#
def make_view_name(name):
    return 'name'


@main.route('/<int:id>/')
@cache.memoize(timeout=20)
def detail(id):
    return render_template('index.html', id=id, now=datetime.datetime.now())


@main.route('/temp/')
def temp_cache():
    return render_template('temp_cache.html', now=datetime.datetime.now())
