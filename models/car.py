
from .base import db ,BaseModel



class Car(BaseModel ,db.Model):
    __tablename__ = 'car'
    id = db.Column(db.Integer, primary_key=True)
    # 車子所屬人
    create_user = db.Column(db.Integer, nullable=False)  # 房

    # 車子名稱
    car_name = db.Column(db.String(20))
    # 車牌號碼
    car_license_plate = db.Column(db.String(10))


