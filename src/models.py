import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), unique=True, nullable=False)
    password = Column(String(8), nullable=False)
    email = Column(String(50), nullable=False)

class Storie(Base):
    __tablename__='storie'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(100))
    author_id = Column(Integer, ForeignKey('user.id'))
    author = relationship(User)

class Photo(Base):
    __tablename__='photo'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(100))
    author_id = Column(Integer, ForeignKey('user.id'))
    author = relationship(User)
    
class Reel(Base):
    __tablename__='reel'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(100))
    author_id = Column(Integer, ForeignKey('user.id'))
    author = relationship(User)

class Post(Base):
    __tablename__= 'post'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('user.id'))
    photo_id = Column(Integer, ForeignKey('photo.id'))
    reel_id = Column(Integer, ForeignKey('reel.id'))
    storie_id = Column(Integer, ForeignKey('storie.id'))
    storie = relationship(Storie)
    reel = relationship(Reel)
    photo = relationship(Photo)
    author = relationship(User)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    author = relationship(User)
    post = relationship(Post)

class Message(Base):
    __tablename__='message'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))
    content_text = Column(String(500))
    user = relationship(User)

class Likes(Base):
    __tablename__='likes'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('user.id'))
    photo_id = Column(Integer, ForeignKey('photo.id'))
    reel_id = Column(Integer, ForeignKey('reel.id'))
    message_id = Column(Integer, ForeignKey('message.id'))
    message = relationship(Message)
    reel = relationship(Reel)
    photo = relationship(Photo)
    author = relationship(User)


class Followers(Base):
    __tablename__='followers'
    id = Column(Integer, primary_key= True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
