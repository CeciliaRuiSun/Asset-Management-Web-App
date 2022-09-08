import string
from flask import Flask, request, abort
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required, current_identity
from marshmallow import Schema, fields
from data import items

class ItemQuerySchema(Schema):
    category = fields.Str()
    name = fields.Str(required=True)
    quantity = fields.Int()
    owner = fields.Str()

schema = ItemQuerySchema()

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
        owner = args.get('owner', None)

        item = {'name': name, 'quantity': quantity, 'category': category, 'owner': owner}
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
        category = args.get('category', None)
        quantity = args.get('quantity', None)
        owner = args.get('owner', None)

        # Once again, print something not in the args to verify everything works
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'quantity': quantity, 'category': category, 'owner': owner}
            items.append(item)
        else:
            item['quantity'] = quantity
            item['category'] = category
            item['owner'] = owner
        return item
