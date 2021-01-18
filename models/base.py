from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()
class BaseModel(object):
    """模型基礎物件"""

    create_time = db.Column(db.DateTime, default=datetime.now)  # 记录的创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)  # 记录的更新时间
