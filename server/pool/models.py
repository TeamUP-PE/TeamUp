from sqlalchemy import Column, String, Integer

from database import Base, db_session


class Model(object):
    def save(self):
        db_session.commit()
        return self

    def create(self):
        db_session.add(self)
        self.save()
        return self


class User(Base, Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(70))
    email = Column(String(70), unique=True)
    password = Column(String(200), nullable=False)

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password

    def __str__(self):
        return self.email

    def create(self, *args, **kwargs):
        super(User, self).create(*args, **kwargs)
