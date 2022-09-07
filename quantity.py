from flask import Flask, request
from flask_restful import Resource, Api

from item import items


class Quantity(Resource):
    def get(self, content, qty):
        args = request.args
        print(args)  # For debugging

        if content == "item_qty_biggerthan":
            return {'item': list(filter(lambda x: x['quantity'] > qty, items))}
        elif content == "item_qty_lessthan":
            return {'item': list(filter(lambda x: x['quantity'] < qty, items))}
        elif content == "item_qty_equalto":
            return {'item': list((filter(lambda x: x['quantity'] == qty, items)))}
        else:
            return "Please put in a valid link. "