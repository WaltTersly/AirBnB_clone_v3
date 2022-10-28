#!/usr/bin/python3
"""index of the application
"""

from api.v1.views import app_views
from flask import jsonify
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
from models.user import User


@app_views.route('/status', strict_slashes=False)
def status():
    """route to the status
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def stats():
    """reurn dictionary count of data
    """
    classes = {
        "amenities": Amenity,
        "cities": City,
        "places": Place,
        "reviews": Review,
        "states": State,
        "users": User}
    dictionary = {}
    for key, cl in classes.items():
        numb = storage.count(cl)
        dictionary[key] = numb
    return jsonify(dictionary)
