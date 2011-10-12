# -*- coding: utf-8 -*-

# Copyright (C) 2011 by Alex Brandt <alunduil@alunduil.com>
#                                                                       
# This program is free software; you can redistribute it andor modify 
# it under the terms of the GNU General Public License as published by 
# the Free Software Foundation; either version 2 of the License, or    
# (at your option) any later version.                                  
#                                                                   
# This program is distributed in the hope that it will be useful,      
# but WITHOUT ANY WARRANTY; without even the implied warranty of       
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        
# GNU General Public License for more details.                         
#                                                                   
# You should have received a copy of the GNU General Public License    
# along with this program; if not, write to the                        
# Free Software Foundation, Inc.,                                      
# 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.            

from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.types import Integer, String, Enum, Text
from sqlalchemy.orm import relation, backref

from breakfast.model.meta import Base

tests_questions_table = Table('tests_questions', Base.metadata, 
        Column('test_id', Integer, ForeignKey('tests.id', onupdate = "CASCADE", ondelete = "CASCADE"), nullable = False),
        Column('question_id', Integer, ForeignKey('questions.id', onupdate = "CASCADE", ondelete = "RESTRICT"), nullable = False),
        )

questions_tags_table = Table('questions_tags', Base.metadata,
        Column('question_id', Integer, ForeignKey('questions.id', onupdate = "CASCADE", ondelete = "CASCADE")),
        Column('tag_id', Integer, ForeignKey('tags.id', onupdate = "CASCADE", ondelete = "CASCADE")),
        )

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key = True)
    question = Column(String(255), nullable = False)
    break_script = Column(Text)
    _rating = Column(Enum("-", "0", "+"), index = True, default = "0", nullable = False)
    _up_votes = Column(Integer, default = 0, nullable = False)
    _down_votes = Column(Integer, default = 0, nullable = False)

    author_id = Column(Integer, ForeignKey('authors.id'), nullable = False)
    author = relation('Author', backref = backref('questions'))

    tests = relation('Test', secondary = tests_questions_table, backref = 'questions')

    tags = relation('Tag', secondary = questions_tags_table, backref = 'questions')

    @property
    def rating(self):
        return self._rating

    @property
    def up_votes(self):
        return self._up_votes

    @property
    def down_votes(self):
        return self._down_votes

    def vote_up(self):
        self._up_votes += 1
        self._update_rating()

    def vote_down(self):
        self._down_votes += 1
        self._update_rating()

    def _update_rating(self):
        delta = self.up_votes - self.down_votes

        window_size = 10

        if delta > window_size:
            self._rating = "+"
        elif delta < -window_size:
            self._rating = "-"
        else:
            self._rating = "0"

    def __repr__(self):
        return "<Question('%s')>" % self.question

