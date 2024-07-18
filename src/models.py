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
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    age = Column(Integer, nullable=False)
    username = Column(String(250), nullable=True)
    password = Column(String(250), nullable=True)
    email = Column(String(100), nullable=True, unique=True)
    favorites = relationship("Favorite", back_populates="user")
    
class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    gender = Column(String(50), nullable=False)
    hair_color = Column(String(50), nullable=False)
    eye_color = Column(String(50), nullable=False)
    birth_year = Column(Integer, nullable=False)
    favorites = relationship("Favorite", back_populates="character")


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    climate = Column(Integer, nullable=False)
    terrain = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    gravity = Column(Integer, nullable=False)
    favorites = relationship("Favorite", back_populates="planet")

class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)
    manufacturer = Column(String(100), nullable=False)
    passengers = Column(Integer, nullable=False)
    favorites = relationship("Favorite", back_populates="starship")

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    starship_id = Column(Integer, ForeignKey('starship.id'))
    add_favorite = Column(String(50), nullable=False)
    delete_favorite = Column(String(50), nullable=False)
    user = relationship("User", back_populates="favorites")
    character = relationship("Character", back_populates="favorites")
    planet = relationship("Planet", back_populates="favorites")
    starship = relationship("Starship", back_populates="favorites")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
