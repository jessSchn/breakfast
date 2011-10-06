"""The application's model objects"""
from breakfast.model.meta import Session, Base

from breakfast.model.test import Test

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)
