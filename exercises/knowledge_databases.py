from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(topic, title, rating):
	topic_object = Knowledge(
		topic = topic,
		title = title,
		rating = rating)
	session.add(topic_object)
	session.commit()
	

def query_all_articles():
	knowledge = session.query(Knowledge).all()
	return(knowledge)

def query_article_by_topic(new_topic):
	knowledge = session.query(Knowledge).filter_by(topic=new_topic).all()
	return(knowledge)

def delete_article_by_topic(new_topic):
	session.query(Knowledge).filter_by(topic=new_topic).delete()
	session.commit()

delete_article_by_topic("food")

def delete_all_articles():
	knowledge = session.query(Knowledge).delete()
	session.commit()

def edit_article_rating(new_rating):
	Knowledge_object = session.query(Knowledge).filter_by(rating = new_rating).first()
	Knowledge_object.rating = new_rating
	session.commit()
	
#add_article("animal", 3, 7)
#add_article("juna", 6, 7)
print(query_article_by_topic("animal"))
#delete_article_by_topic("juna")
delete_all_articles()
print(query_all_articles())

