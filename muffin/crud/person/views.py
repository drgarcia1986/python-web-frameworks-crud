# -*- coding: utf-8 -*-
import json

from playhouse.shortcuts import model_to_dict

from .. import app, muffin
from .models import Person


@app.register('/api/persons/')
class PersonListCreate(muffin.Handler):

    def get(self, request):
        return {'objects': [model_to_dict(p) for p in Person.select()]}

    def post(self, request):
        person_dict = yield from request.json()
        person = Person.create(
            email=person_dict['email'],
            name=person_dict['name']
        )
        return muffin.Response(
            text=json.dumps(model_to_dict(person)),
            status=201,
            content_type='application/json'
        )


@app.register('/api/persons/{cod}/')
class PersonRetriverUpdateDestroy(muffin.Handler):

    def _get_person(self, request):
        try:
            person = Person.get(
                Person.cod == request.match_info.get('cod')
            )
            return person
        except Person.DoesNotExist:
            raise muffin.HTTPNotFound()

    def get(self, request):
        person = self._get_person(request)
        return model_to_dict(person)

    def put(self, request):
        person = self._get_person(request)
        person_dict = yield from request.json()
        person.name = person_dict['name']
        person.email = person_dict['email']
        person.save()
        return model_to_dict(person)

    def delete(self, request):
        person = self._get_person(request)
        person.delete().execute()
        return muffin.Response(text='', status=204)
