# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify

from .models import Person


person_bp = Blueprint('person', __name__)


@person_bp.route('/', methods=['GET', 'POST'])
def listing_create():
    if request.method == 'GET':
        return jsonify(
            objects=[p.as_dict() for p in Person.query.all()]
        )
    else:
        person_dict = request.get_json()
        person = Person(
            email=person_dict['email'],
            name=person_dict['name']
        )
        person.save()
        return jsonify(person.as_dict()), 201


@person_bp.route('/<person_cod>/', methods=['GET', 'PUT', 'DELETE'])
def retriver_update_destroy(person_cod):
    person = Person.query.get_or_404(person_cod)
    if request.method == 'GET':
        return jsonify(person.as_dict())
    elif request.method == 'PUT':
        person_dict = request.get_json()
        person.email = person_dict['email']
        person.name = person_dict['name']
        person.save()
        return jsonify(person.as_dict()), 200
    else:
        person.delete()
        return '', 204
