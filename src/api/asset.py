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
            {
                "id": row[0], 
                "name": row[1], 
                "type": row[2], 
                "serial_number": row[3], 
                "operating_system": row[4]
            }
            for row in result
        ]

        if assets: 
            return jsonify(assets)
        else: # If our list of assets we obtain is empty, it will be 'False' and return an error message instead
            return "Cyber Assets not found"
    
    def post(self):
        args = body_parser.parse_args()

        new_asset_name = args['NAME']
        new_asset_type = args['TYPE']
        new_asset_serial_number = args['SERIAL_NUMBER']
        new_operating_system = args['OPERATING_SYSTEM']

        post_sql_query = """ 
            INSERT INTO CYBER_ASSET(NAME, TYPE, SERIAL_NUMBER, OPERATING_SYSTEM)
            VALUES (?, ? , ?, ?)
        """

        new_asset_id = exec_insert_returning(post_sql_query, (new_asset_name, new_asset_type, new_asset_serial_number, new_operating_system))
        return f"Cyber Asset with the id: {new_asset_id} created successfully"

class AssetsID(Resource):
    def get(self, id):
        get_sql_query = "SELECT * FROM CYBER_ASSET WHERE ID=?"
        asset = exec_get_one(get_sql_query, (id,))

        if asset is not None:
            asset_dict = {
                "id": asset[0],
                "name": asset[1],
                "type": asset[2],
                "serial_number": asset[3],
                "operating_system": asset[4]
            }
            return asset_dict
        else:
            return "Cyber Asset not found"

    def delete(self, id):
        pass