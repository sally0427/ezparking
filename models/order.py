from .base import db,BaseModel
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import TEXT, MEDIUMTEXT
from datetime import datetime
from sqlalchemy import text


class Order(BaseModel,db.Model):
    ''' 訂單 '''
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)  # 下订单的用户编号
    # order_id = db.Column(db.Integer, index=True)
    # 哪一台車
    car_id = db.Column(db.Integer, db.ForeignKey("car.id"), nullable=False)
    # 用哪張卡付款
    credit_card_id = db.Column(db.Integer, db.ForeignKey("credit_card.id"))

    order_comment = db.Column(db.String(300))
    order_price = db.Column(db.Integer)
    order_counting_time = db.Column(db.DateTime)
    order_status = db.Column(  # 订单的状态
        db.Enum(
            "WAIT_PAYMENT",  # 待支付
            "COMPLETE",  # 已完成
        ),
        default="WAIT_PAYMENT", index=True)

    def __init__(self, data):
        self.create_order(data)

    def create_order(self, data):
        self.user_id = data['user_id']
        self.car_id = data['car_id']
        pass

    # db.Index('ix_book_id_user_id', book_id, user_id, unique=True)

