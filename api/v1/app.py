#!/usr/bin/python3
"""Status of API"""

from flask import Flask
from api.v1.views import app_views
from models import storage
from os import getenv



app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(error):
    """Call storage.close()"""
    storage.close()
    
@app.errorhandler(404)
def page_not_found(error):
    """
    handler error 404
    """
    return (jsonify(error="Not found"), 404)


if __name__ == "__main__":
    app.run(host=getenv('HBNB_API_HOST'),
            port=getenv('HBNB_API_PORT'),
            threaded=True)
