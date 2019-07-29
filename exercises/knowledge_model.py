from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__ = 'students'
	article_id = Column(Integer, primary_key=True)
	topic = Column(String)
	title = Column(Integer)
	rating = Column(Integer)

	def __repr__(self):
		return("ID: {}\n"
			   "Article topic: {}\n"
			   "Article title: {}\n"
			   "Article rating: {}").format(
			   self.article_id,
			   self.topic,
			   self.title,
			   self.rating)