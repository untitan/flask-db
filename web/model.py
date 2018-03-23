from web import db

print('加载：', 'model')


class PpMsg(db.Model):
    __tablename__ = 'pp_msg'
    id = db.Column(db.String(42), primary_key=True)
    msg = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<PpMsg : %s>' % (self.msg)
