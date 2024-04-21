from flask_restful import Resource, reqparse
from db.db_utils import *

body_parser = reqparse.RequestParser()
body_parser.add_argument('NAME', type=str,  location='json')
body_parser.add_argument('TYPE', type=str, location='json')
body_parser.add_argument('SERIAL_NUMBER', type=str, location='json')
body_parser.add_argument('OPERATING_SYSTEM', type=str, location='json')

class Assets(Resource):
    def get(self):
        pass
    
    def post(self):
        pass

class AssetsID(Resource):
    def get(self, id):
        pass

    def delete(self, id):
        pass