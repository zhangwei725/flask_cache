import datetime

from apps.ext import db


# backref
class User(db.Model):
    uid = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(100), unique=True, index=True, nullable=False)
    image = db.relationship('Image', back_populates='user', uselist=False)


# dynamic 选项只能用于一对多或者多对多关系
class Image(db.Model):
    img_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    path = db.Column(db.String(255), unique=True, default='')
    # 1  表示用户头像  2表示商品的信息
    type = db.Column(db.SmallInteger, nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.datetime.now())
    # 外键字段
    # 查询的字段
    uid = db.Column(db.Integer, db.ForeignKey(User.uid), unique=True)
    user = db.relationship('User', back_populates='image', uselist=False)


"""
建立外键   外键约束
一对一  一对多(多对一) 多对多
"""
