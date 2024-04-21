from flask import jsonify
from flask_restful import Resource, reqparse
from db.db_utils import *

body_parser = reqparse.RequestParser()
body_parser.add_argument('NAME', type=str,  location='json')
body_parser.add_argument('TYPE', type=str, location='json')
body_parser.add_argument('SERIAL_NUMBER', type=str, location='json')
body_parser.add_argument('OPERATING_SYSTEM', type=str, location='json')

class Assets(Resource):
    def get(self):
        get_sql_query = "SELECT * FROM CYBER_ASSET"
        result = exec_get_all(get_sql_query)

        assets = [
            dict(id=row[0], name=row[1], type=row[2], serial_number=row, operating_system=row[4])
            for row in result
        ]

        if assets:
            return assets
        else:
            return "Assets not found"
    
    def post(self):
        pass

class AssetsID(Resource):
    def get(self, id):
        pass

    def delete(self, id):
        pass