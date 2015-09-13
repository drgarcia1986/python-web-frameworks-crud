# -*- coding: utf-8 -*-

import sqlalchemy as sa

from crud import db
from sqlalchemy.exc import InvalidRequestError, IntegrityError


class Person(db.Base):
    __tablename__ = 'persons'
    cod = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    email = sa.Column(sa.String(120), unique=True)
    name = sa.Column(sa.String(50))

    def __init__(self, email, name):
        self.email = email
        self.name = name

    def __repr__(self):
        return '<Person {}>'.format(self.name)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def as_dict(self):
        return {
            'cod': self.cod,
            'email': self.email,
            'name': self.name
        }

    @classmethod
    def create(cls, email, name):
        try:
            person = cls(email, name)
            person.save()
            return person
        except InvalidRequestError as e:
            db.session.rollback()
        except IntegrityError as e:
            db.session.rollback()
        except Exception as e:
            db.session.rollback()
        return e

Person.metadata.create_all()
