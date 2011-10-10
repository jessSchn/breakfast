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

from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String, Enum
from sqlalchemy.orm import relation, backref

from breakfast.model.meta import Base

class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key = True))
    check_script = Column(Text)
    answer = Column(String(255))
    
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relation('Author', backref = backref('answers'))

    question_id = Column(Integer, ForeignKey('question.id'), index = True)
    question = relation('Question', backref = backref('answers'))

    def __repr__(self):
        return "<Tag('%s')>" % self.name

