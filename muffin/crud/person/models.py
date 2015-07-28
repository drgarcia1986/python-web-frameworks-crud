# -*- coding: utf-8 -*-
import peewee

from .. import app


@app.ps.peewee.register
class Person(peewee.Model):
    cod = peewee.IntegerField(primary_key=True)
    email = peewee.CharField(unique=True)
    name = peewee.CharField()
