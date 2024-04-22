from flask import jsonify
from flask_restful import Resource, reqparse
from db.db_utils import *
from http import HTTPStatus

query_parser = reqparse.RequestParser()
query_parser.add_argument('type', type=str, location='args')

body_parser = reqparse.RequestParser()
body_parser.add_argument('NAME', type=str,  location='json')
body_parser.add_argument('TYPE', type=str, location='json')
body_parser.add_argument('SERIAL_NUMBER', type=str, location='json')
body_parser.add_argument('OPERATING_SYSTEM', type=str, location='json')

class Assets(Resource):
    def get(self):
        args = query_parser.parse_args()
        asset_type = args['type']

        get_sql_query = "SELECT * FROM CYBER_ASSET"

        if asset_type is not None: # If 'type' parameter is provided, filter cyber assets by type
            get_sql_query += " WHERE TYPE=?"
            result = exec_get_all(get_sql_query, (asset_type,))
        else: # Otherwise, fetech all cyber assets in the database like normal
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
            return ({"assets": assets}), HTTPStatus.OK
        else: # If our list of assets we obtain is empty, it will be 'False' and return an error message instead
            return "Cyber assets not found", HTTPStatus.NOT_FOUND
    
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

        try:
            new_asset_id = exec_insert_returning(post_sql_query, (new_asset_name, new_asset_type, new_asset_serial_number, new_operating_system))
            return f"Cyber asset with the id: {new_asset_id} created successfully", HTTPStatus.CREATED
        except Exception as e:
            return f"Error creating cyber asset: {str(e)}", HTTPStatus.INTERNAL_SERVER_ERROR

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
            return "Cyber asset not found", HTTPStatus.NOT_FOUND

    def put(self, id):
        args = body_parser.parse_args()

        new_asset_name = args['NAME']
        new_asset_type = args['TYPE']
        new_asset_serial_number = args['SERIAL_NUMBER']
        new_operating_system = args['OPERATING_SYSTEM']

        updated_asset = {
            "id": id,
            "name": new_asset_name,
            "type": new_asset_type,
            "serial_number": new_asset_serial_number,
            "operating_system": new_operating_system
        }
        
        put_sql_query = """ 
            UPDATE ASSET SET
            NAME=?,
            TYPE=?,
            SERIAL_NUMBER=?,
            OPERATING_SYSTEM=?
            WHERE ID=?
        """ 
        
        rows_affected = exec_commit(put_sql_query, (new_asset_name, new_asset_type, new_asset_serial_number, new_operating_system, id))

        if rows_affected > 0:
            return updated_asset, HTTPStatus.OK
        else:
            return "Cyber asset not found or update failed", HTTPStatus.NOT_FOUND

    def delete(self, id):
        delete_sql_query = """ DELETE FROM CYBER_ASSET WHERE ID=? """
        rows_affected = exec_commit(delete_sql_query, (id,))
        
        if rows_affected > 0:
            return f"The cyber asset with id: {id} has been deleted.", HTTPStatus.OK
        else:
            return "Cyber asset not found or already deleted", HTTPStatus.NOT_FOUND