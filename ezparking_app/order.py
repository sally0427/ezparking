from flask import Blueprint,request,jsonify
from authlib.integrations.flask_client import OAuth
from flask import Flask, redirect, url_for, session,g
from flask import current_app
from models import User,db,Order,Car
from utils.commons import login_required

from utils.response_code import RET
order_bp = Blueprint('order_bp',__name__,url_prefix='/order')

@order_bp.route('/',methods=['POST'])
@login_required
def create_order():
    car_id = request.args.get("car_id")

    if not car_id:
        return jsonify(errno=RET.PARAMERR, errmsg="參數錯誤")


    user_id =  g.user_id
    # User.query.filter(User.cars == user_id, Car.id == car_id).first()
    # find if car exist
    user = User.query.filter(User.id == user_id).first()
    user_car = None

    for car in user.cars:
        print(car.id)
        if str(car.id) == str(car_id):
            user_car = car

    if not user_car:
        return jsonify(errno=RET.REQERR, errmsg="您無此車輛")
    # if not car:
    #     return jsonify(errno=RET.REQERR, errmsg="無此車輛")

    # find if order exist
    exist_order = Order.query.filter(Order.user_id == user_id,Order.order_status == 'WAIT_PAYMENT').first()
    if exist_order:
        return jsonify(errno=RET.REQERR, errmsg="訂單已存在")

    order_info = dict(
        user_id=user_id,
        car_id = user_car.id
    )
    order = Order(order_info)
    db.session.add(order)
    db.session.commit()
    return jsonify(errno=RET.OK, errmsg="OK", data={"order": 1})