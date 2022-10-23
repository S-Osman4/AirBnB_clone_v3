#!/usr/bin/python3
"""
objects that handles all default RestFul API actions:
"""
from flask import Flask, jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.city import City
from models.state import State
