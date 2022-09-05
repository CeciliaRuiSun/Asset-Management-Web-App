import string

from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity

items = [{'category':'Office Supply', 'name':'Table', 'quantity': 2}]

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('quantity',
        type=int,
        required=True,
        help="This field cannot be left blank!"
    )

    parser.add_argument('category',
        type=string,
        required=True,
        help="This field cannot be left blank!"
        )

    @jwt_required()
    def get(self, name):
        print("GET,", name)
        return {'item': next(filter(lambda x: x['name'] == name, items), None)}

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with name '{}' already exists.".format(name)}

        data = Item.parser.parse_args()

        item = {'name': name, 'quantity': data['quantity'], 'category': data['category']}
        items.append(item)
        return item

    @jwt_required()
    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        # Once again, print something not in the args to verify everything works
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'quantity': data['quantity'], 'category': data['category']}
            items.append(item)
        else:
            item.update(data)
        return item