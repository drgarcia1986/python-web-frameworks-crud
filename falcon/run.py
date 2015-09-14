# -*- coding: utf-8 -*-

import falcon

from crud.person.resource import PersonResource

api = falcon.API()
api.add_route('/api/persons', PersonResource())
api.add_route('/api/persons/{cod}', PersonResource())

# gunicorn run:api -b 127.0.0.1:8080
