from flask import Flask
from flask_restful import Api
from api.asset import *
from db.init_db import initialize_sqlite_db

app = Flask(__name__)
api = Api(app)

api.add_resource(Assets, '/assets')
api.add_resource(AssetsID, '/assets/<int:id>')

if __name__ == '__main__':
    initialize_sqlite_db()
    app.run(debug=True)
