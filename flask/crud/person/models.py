# -*- coding: utf-8 -*-
from crud.extensions import db


class Person(db.Model):
    __tablename__ = 'persons'
    cod = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    name = db.Column(db.String(50))

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
        person = cls(email, name)
        person.save()

        return person
