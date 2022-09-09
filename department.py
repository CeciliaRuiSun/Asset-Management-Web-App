from flask import Flask, request, abort
from flask_restful import Resource, Api

from data import items, person
from marshmallow import Schema, fields

class DeptQuerySchema(Schema):
    category = fields.Str()
    name = fields.Str()
    quantity = fields.Int()
    owner = fields.Str()
    department = fields.Str(required=True)

schema = DeptQuerySchema()

class Dept(Resource):

    def get(self):
        errors = schema.validate(request.args)
        if errors:
            abort(400, str(errors))
        args = request.args
        dept = args['department']
        ID = []
        dept_items = []
        for p in person:
            if p['department'] == dept:
                ID.append(p['ID'])
        for item in items:
            if item['employee_id'] in ID:
                dept_items.append(item)

        return dept_items
