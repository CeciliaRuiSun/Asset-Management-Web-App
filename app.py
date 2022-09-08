from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity

from item import Item
from quantity import Quantity
from security import authenticate, identity

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.secret_key = 'jose'
api = Api(app)


jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item', endpoint='item')
api.add_resource(Quantity, '/qty', endpoint='qty')

if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True




