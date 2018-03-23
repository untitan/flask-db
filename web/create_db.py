from web import db

import config

print('加载：', 'create_db')

if config.IS_CREATE_DB:
    print('开始创建数据库表')
    db.drop_all()
    db.create_all()
