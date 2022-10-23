#!/usr/bin/python3
"""
 New view for Places objects that handles all default RestFul API actions.
"""
from models.place import Place
from models.city import City
from models import storage
from flask import Flask, request, jsonify, abort
from api.v1.views import app_views
