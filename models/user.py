from .base import BaseModel,db
from flask_login import UserMixin
from sqlalchemy.sql import func
from .car import Car
user_cars_relation = db.Table(
    'user_cars_relation',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('car_id', db.Integer, db.ForeignKey('car.id')))

class User(BaseModel,UserMixin, db.Model):
    """ 使用者 """
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(128), unique=True)
    name = db.Column(db.String(128), unique=True)
    openId = db.Column(db.String(128), unique=True)
    userType = db.Column(db.SmallInteger(),default=0) # 0: 普通使用者 1: VIP
    avatarUrl = db.Column(db.String(200))
    modified = db.Column(db.DateTime(), server_default=func.now())
    orders = db.relationship("Order", backref="user")  # 用户下的订单
    cars = db.relationship("Car", secondary=user_cars_relation,backref="user")
    credit_cards = db.relationship("CreditCard", backref="user")

    def __init__(self, data):
        self.update_info(data)

    def update_info(self, data):
        self.openId = data['id']
        self.email = data['email']
        self.name = data['name']
        pass


