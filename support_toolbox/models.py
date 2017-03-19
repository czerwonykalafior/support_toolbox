# coding: utf-8
import json

from sqlalchemy import Column, Integer, String
from sqlalchemy import Date
from sqlalchemy.ext.declarative import declarative_base
from flask_jsontools import JsonSerializableBase


Base = declarative_base(cls=(JsonSerializableBase,))
metadata = Base.metadata

class RobotWip(Base):
    __tablename__ = 'ops_wip'

    pk = Column(Integer, primary_key=True)
    robot_name = Column(String(248))
    web_miner = Column(String(10))


class RobotLog(Base):
    __tablename__ = 'robot_log'

    pk = Column(Integer, primary_key=True)
    robot_name = Column(String(248))
    starttime = Column(Date)
    endtime = Column(Date)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'id'         : self.pk,
           'robot_name': self.robot_name
       }

