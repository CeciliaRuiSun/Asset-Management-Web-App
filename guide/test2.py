from flask import Flask, request, abort
from flask_restful import Resource, Api
from marshmallow import Schema, fields


class BarQuerySchema(Schema):
    key1 = fields.Str(required=True)
    key2 = fields.Str(required=True)
    kucundayu = fields.Int()


app = Flask(__name__)
api = Api(app)
schema = BarQuerySchema()


class BarAPI(Resource):
    def get(self):
        print(request.args)
        errors = schema.validate(request.args)
        if errors:
            abort(400, str(errors))
        msg = "OK"
        #print(request.args['key1'])
        msg += request.args['key1'] + ", "
        #print(request.args['key1'])
        msg += request.args['key2'] + ", "

        if 'kucundayu' in request.args:
            print(request.args['kucundayu'])
            msg += request.args['kucundayu'] + ", "
        return msg

api.add_resource(BarAPI, '/bar', endpoint='bar')

# omit of you intend to use `flask run` command
if __name__ == '__main__':
    app.run(debug=True)