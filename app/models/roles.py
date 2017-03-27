from app.models import db


class Role(db.Model):
    __tablename__ = 'roles'

    role_pk = db.Column(db.SmallInteger, primary_key=True)
    title = db.Column(db.String(32))
