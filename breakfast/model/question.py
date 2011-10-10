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

from breakfast.model.meta import Base, metadata

tests_questions_table = Table('tests_questions', metadata, 
        Column('test_id', Integer, ForeignKey('test.id', onupdate = "CASCADE", ondelete = "CASCADE")),
        Column('question_id', Integer, ForeignKey('question.id', onupdate = "CASCADE", ondelete = "RESTRICT")),
        )

questions_tags_table = Table('questions_tags', metadata,
        Column('question_id', Integer, ForeignKey('question.id', onupdate = "CASCADE", ondelete = "CASCADE")),
        Column('tag_id', Integer, ForeignKey('tag.id', onupdate = "CASCADE", ondelete = "CASCADE")),
        )

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key = True)
    question = Column(String(255))
    break_script = Column(Text)
    rating = Column(Enum("-", None, "+"), index = True)
    up_votes = Column(Integer)
    down_votes = Column(Integer)

    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relation('Author', backref = backref('questions'))

    tests = relation('Test', secondary = tests_questions_table, backref = 'questions')

    tags = relation('Tag', secondary = questions_tags_table, backref = 'questions')

    def __repr__(self):
        return "<Question('%s')>" % self.question

