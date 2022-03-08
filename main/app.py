from flask import Flask

from main.zone_controller import ZoneController


def create_app():
    app = Flask(__name__)
    ZoneController().register(app)
    return app
