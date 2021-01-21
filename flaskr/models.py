from sqlalchemy import Column, String, Text, Integer, DateTime, ForeignKey
from datetime import datetime
from flaskr import db


class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    username = Column(String(20), nullable=False, unique=True)
    password = Column(String(100))
    status = Column(String(20), default='NORMAL')
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)

    def __repr__(self):
        return "User( \
            username='{self.username}',\
            password='{self.password}',\
            status={self.status},\
            )".format(self=self)


class Post(db.Model):
    __tablename__ = 'post'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    author_id = Column(None, ForeignKey('user.id'))
    title = Column(String(50))
    body = Column(Text(1000))
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)

    def __repr__(self):
        return "Post(\
            author_id='{self.author_id}',\
            title={self.title},\
            body={self.body},\
            created_at={self.created_at}\
            )".format(self=self)
