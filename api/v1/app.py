#!/usr/bin/pyhon3
"""creating instance of flask
"""
from api.v1.views import app_views
from flask import Flask
from models import storage
import os

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown():
    """allows to close the session
    """
    storage.close()


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', default='0.0.0.0')
    port = os.getenv('HBNB_API_PORT', default='5000')
    app.run(host=host, port=int(port), threaded=True)
