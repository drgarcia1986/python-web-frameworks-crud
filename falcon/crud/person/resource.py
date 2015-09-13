# -*- coding: utf-8 -*-

import json

import falcon

from .models import Person


class PersonResource(object):

    def decode_json(self, req):
        try:
            raw_json = req.stream.read()
            print raw_json
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Error',
                                   ex.message)
        try:
            decoded_json = json.loads(raw_json, encoding='utf-8')
        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Invalid JSON',
                                   'Could not decode the request body. The '
                                   'JSON was incorrect.')
        return raw_json, decoded_json

    def on_get(self, req, resp, cod=None):
        if cod:
            persons = Person.query.filter_by(cod=cod).all()
        else:
            persons = Person.query.all()

        if persons:
            result = {'objects': [p.as_dict() for p in persons]} if not cod else persons[0].as_dict()
            resp.body = json.dumps(result)
        else:
            raise falcon.HTTPError(falcon.HTTP_404, 'No entry')

    def on_post(self, req, resp):
        raw_json, decoded_json = self.decode_json(req)

        result = Person.create(decoded_json['email'], decoded_json['name'])
        if isinstance(result, Person):
            resp.body = json.dumps(result.as_dict())
            resp.status = falcon.HTTP_201
        elif isinstance(result, Exception):
            resp.body = json.dumps({'error': result.message})
            resp.status = falcon.HTTP_400

    def on_put(self, req, resp, cod=None):
        if not cod:
            raise falcon.HTTPError(falcon.HTTP_400, 'Error', 'Please provide cod')
        raw_json, decoded_json = self.decode_json(req)
        p = Person.query.filter_by(cod=cod).update({'email': decoded_json['email'], 'name': decoded_json['name']})
        if p:
            persons = Person.query.filter_by(cod=cod)
            resp.body = json.dumps({'objects': [p.as_dict() for p in persons]} if not cod else persons[0].as_dict())
        else:
            raise falcon.HTTPError(falcon.HTTP_404, 'No entry')

    def on_delete(self, req, resp, cod=None):
        if not cod:
            raise falcon.HTTPError(falcon.HTTP_400, 'Error', 'Please provide cod')
        persons = Person.query.filter_by(cod=cod)
        if persons:
            for p in persons:
                p.delete()
            resp.status = falcon.HTTP_204
        else:
            raise falcon.HTTPError(falcon.HTTP_404, 'No entry')
