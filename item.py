import string
from flask import Flask, request, abort
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required, current_identity
from marshmallow import Schema, fields

items = [{'category': 'O1', 'name': 'T1', 'quantity': 2}, {'category': 'O2', 'name': 'T2', 'quantity': 10},
         {'category': 'O3', 'name': 'T3', 'quantity': 8}, {'category': 'O4', 'name': 'T4', 'quantity': 2},
         {'category': 'O5', 'name': 'T5', 'quantity': 2}]


class BarQuerySchema(Schema):
    category = fields.Str()
    name = fields.Str(required=True)
    quantity = fields.Int()


schema = BarQuerySchema()

class Item(Resource):

    @jwt_required()
    def get(self):
        errors = schema.validate(request.args)
        if errors:
            abort(400, str(errors))
        args = request.args
        name = args['name']
        return {'item': next(filter(lambda x: x['name'] == name, items), None)}

    def post(self):
        args = request.args
        name = args['name']
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with name '{}' already exists.".format(name)}

        category = args.get('category',None)
        quantity = args.get('quantity',None)

        item = {'name': name, 'quantity': quantity, 'category': category}
        items.append(item)
        return {'item': next(filter(lambda x: x['name'] == name, items), None)}

    @jwt_required()
    def delete(self):
        global items
        args = request.args
        name = args['name']
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    @jwt_required()
    def put(self):
        args = request.args
        name = args['name']
        category = args['category']
        quantity = args['quantity']
        # Once again, print something not in the args to verify everything works
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'quantity': quantity, 'category': category}
            items.append(item)
        else:
            item['quantity'] = quantity
            item['category'] = category
        return item
