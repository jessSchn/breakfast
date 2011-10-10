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
from sqlalchemy.types import Integer, String, Boolean, Text
from sqlalchemy.orm import relation, backref

from Crypto.Hash import SHA256

from breakfast.model.meta import Base

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, index = True)
    username = Column(String(255), primary_key = True)
    email = Column(String(255))
    grader = Column(Boolean)
    _password = Column(Text)
    admin = Column(Boolean)

    @property
    def password(self):
        return _password

    @password.setter
    def password(self, value):
        cypher = SHA256.new()
        cypher.update(value)
        _password = cypher.digest()

    def __repr__(self):
        return "<Author('%s')>" % self.name

