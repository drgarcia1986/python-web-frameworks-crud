# -*- coding: utf-8 -*-


import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import scoped_session, sessionmaker

session = DBSession = scoped_session(sessionmaker())


class BaseMixin(object):
    query = DBSession.query_property()

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

Base = declarative_base(cls=BaseMixin)
engine = sa.create_engine('sqlite:///database.db')
engine.echo = True
Base.metadata.bind = engine
