#!/usr/bin/python3
"""create API with flask"""

from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage
from os import getenv
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown(error):
    """Call storage.close()"""
    storage.close()
    
@app.errorhandler(404)
def page_not_found(error):
    """
    handler error 404
    """
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run(host=getenv('HBNB_API_HOST'),
            port=getenv('HBNB_API_PORT'),
            threaded=True)
