#!/usr/bin/python3
"""Home page"""

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', strict_slashes=False)
def status():
    """Return status: OK"""
    return jsonify({'status': 'OK'})
