# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class RobotWip(Base):
    __tablename__ = 'ops_wip'

    pk = Column(Integer, primary_key=True)
    robot_name = Column(String(248))
    web_miner = Column(String(10))
