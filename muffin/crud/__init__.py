# -*- coding: utf-8 -*-
import muffin


app = muffin.Application(
    'crud',
    PLUGINS=(
        'muffin_peewee',
    ),
    PEEWEE_CONNECTION='sqlite:///database.db',
)


from .person.views import *  # noqa


@app.manage.command
def create_db():
    from .person.models import Person  # noqa
    app.ps.peewee.database.create_table(Person)
