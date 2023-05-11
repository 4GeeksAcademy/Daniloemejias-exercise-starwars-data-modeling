import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year= Column(String(15), nullable=False)
    eye_color= Column(String(10), nullable=False)
    films_id=Column(Integer, ForeignKey("films.id"))
    gender=Column(String(10), nullable=False)
    hair_color=Column(String(10), nullable=False)
    height=Column(Float, nullable=False)
    homeworld_id= Column(Integer, ForeignKey("planets.id"))
    planet=relationship("Planets")
    # species="https://swapi.dev/api/species/1/"
    # starships="https://swapi.dev/api/starships/12/"

class Cast(Base):
    __tablename__ = 'cast'
    id = Column(Integer, primary_key=True)
    film_id=Column(Integer, ForeignKey("films.id"))
    film=relationship("Films", backref="cast")
    people_id=Column(Integer, ForeignKey("people.id"))
    people=relationship("People")

    


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate= Column(String(15), nullable=False)
    gravity= Column(String(10), nullable=False)
    # films=https://swapi.dev/api/films/1/"
    terrain=Column(String(10), nullable=False)
    population=Column(Float, nullable=False)
    orbital_period=Column(Float, nullable=False)
#    "residents"= "https://swapi.dev/api/people/1/"
   

class Films(Base):
    __tablename__ = 'films'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    characters = Column(String(250), nullable=False)
    director= Column(String(15), nullable=False)
    episode_id= Column(String(10), nullable=False)
    # films=https://swapi.dev/api/films/1/"
    #    "residents"= "https://swapi.dev/api/people/1/"
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
