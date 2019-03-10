#!/usr/bin/python3

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    @property
    def serialize(self):
        return {
           'name': self.name,
           'id': self.id,
        }


class Breed(Base):
    __tablename__ = 'breed'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(500))
    rank = Column(Integer)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    photo = Column(String(250))
    photo_attribution = Column(String(250))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id,
            'description': self.description,
            'rank': self.rank,
            'photo': self.photo,
            'photo_attribution': self.photo_attribution,
            'category_id': self.category_id
        }

engine = create_engine('sqlite:///catalog_proj.db')


Base.metadata.create_all(engine)
