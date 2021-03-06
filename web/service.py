from web import db
from web.model import PpMsg


def add_msg(msgid, msg, content):
    msg = PpMsg(id=msgid, msg=msg, content=content)
    db.session.add(msg)
    db.session.commit()


def query_fetch(msg):
    return PpMsg.query.filter(PpMsg.msg == msg).all()


def query_all():
    return PpMsg.query.all()
