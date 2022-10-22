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
    cls_list = ["Amenity", "City", "Place",
                "Review", "State", "User"]
    cls_output = ["amenities", "cities", "places",
                  "reviews", "states", "users"]
    cls_count = {}
    for index in range(len(cls_list)):
        cls_count[cls_output[index]] = storage.count(cls_list[index])
    return jsonify(cls_count)
