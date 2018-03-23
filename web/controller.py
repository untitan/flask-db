import uuid

from flask import render_template

from web import app, service

print('加载：', 'controller')


@app.route('/')
def index():
    return 'index'


@app.route('/add')
def add():
    service.add_msg(str(uuid.uuid1()), 'push', '奔跑的花卷')
    return 'added'


@app.route('/query/<msg>')
def query(msg):
    msg_list = service.query_fetch(msg)
    return render_template('msg.html', msg_list=msg_list)


@app.route('/query')
def queryall():
    msg_list = service.query_all()
    return render_template('msg.html', msg_list=msg_list)
