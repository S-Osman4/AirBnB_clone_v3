#!/usr/bin/python3
"""
 New view for Amenities objects that handles all default RestFul API actions.
"""
from models.amenity import Amenity
from models import storage
from flask import Flask, request, jsonify, abort
from api.v1.views import app_views
