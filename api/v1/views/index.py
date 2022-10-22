#!/usr/bin/python3
"""
Status of our Api and some stats.
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status")
def app_status():
    """
    Simply returns the state of the api.
    """
    return(jsonify(status="OK"))


@app_views.route("/stats")
def stats():
    """
    Returns statistics about the number of objects available.
    """
     total_cls = {"amenities": Amenity,
                 "cities": City,
                 "places": Place,
                 "reviews": Review,
                 "states": State,
                 "users": User}
    count = {key: storage.count(val) for key, val in total_cls.items()}
    return jsonify(count)
