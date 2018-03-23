from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 设置默认的level为DEBUG
# 设置log的格式


print('加载：', 'web.__init__.py')

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from web import model

from web import create_db

from web import controller
