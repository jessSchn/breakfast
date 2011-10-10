"""The application's model objects"""
from breakfast.model.meta import Session, Base

from breakfast.model.test import Test
from breakfast.model.question import Question
from breakfast.model.tag import Tag
from breakfast.model.answer import Answer
from breakfast.model.author import Author

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)
