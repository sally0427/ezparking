

from .base import db,BaseModel
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import TEXT, MEDIUMTEXT
from datetime import datetime
from sqlalchemy import text


class CreditCard(BaseModel,db.Model):
    __tablename__ = 'credit_card'
    id = db.Column(db.Integer, primary_key=True)
    # 信用卡所屬人
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    # 信用卡種類
    credit_card_type = db.Column(db.SmallInteger)
    # 信用卡卡號
    credit_card_num = db.Column(db.String(64))


