import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    Favorites_id = Column(Integer, ForeignKey('favorites.id'))


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    height = Column(String(250))
    Favorites_id = Column(Integer, ForeignKey('favorites.id'))


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    gravity = Column(String(250))
    Favorites_id = Column(Integer, ForeignKey('favorites.id'))


class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    Character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)
    Planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
