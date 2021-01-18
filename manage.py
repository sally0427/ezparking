from flask import Flask,Blueprint
# 導入擴展
from flask_sqlalchemy import SQLAlchemy
# 腳本
from flask_script import Manager

# 數據庫
from flask_migrate import Migrate,MigrateCommand
from ezparking_app import create_app
# 導入配置字典
from config import config_dict
app = create_app(config_dict['dev_config'])
from models import db

#
# db = SQLAlchemy(app)

#腳本管理器
manager = Manager(app)
# 遷移框架
Migrate(app,db)
# 添加遷移命令
manager.add_command('db',MigrateCommand)


@app.route("/")
def index():
    return 'index info'




if __name__ == '__main__':
    print(app.url_map)
    manager.run()