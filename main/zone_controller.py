from flask import request


class ZoneController:
    def __init__(self):
        self.zones = {}

    def register(self, app):
        app.route('/v1/zones/<id>')(self.get)
        app.route('/v1/zones/<id>', methods=['POST'])(self.create)
        app.route('/v1/zones/<id>', methods=['DELETE'])(self.delete)
        app.route('/v1/zones/<id>', methods=['PUT'])(self.update)

    def get(self, id):
        if id in self.zones:
            return self.zones[id]
        else:
            return {'error': f'zone \'{id}\' does not exist'}, 404

    def create(self, id):
        zone = {'groups': []}
        self.zones[id] = zone
        return zone

    def delete(self, id):
        del self.zones[id]
        return {'message': f'successfully deleted zone \'{id}\''}

    def update(self, id):
        if id in self.zones:
            zone = request.json
            self.zones[id] = zone
            return zone
        else:
            return {'error': f'zone \'{id}\' does not exist'}, 404
