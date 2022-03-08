from uuid import uuid4


def test_create_delete_zone(zone_client):
    id = uuid4()

    assert zone_client.get(id, expect_status=404) == {'error': f'zone \'{id}\' does not exist'}
    assert zone_client.create(id) == {'groups': []}
    assert zone_client.get(id) == {'groups': []}
    assert zone_client.delete(id) == {'message': f'successfully deleted zone \'{id}\''}
    assert zone_client.get(id, expect_status=404) == {'error': f'zone \'{id}\' does not exist'}


def test_update_zone(zone_client):
    id, zone = uuid4(), {'groups': [{'name': 'my first group'}]}

    assert zone_client.update(id, zone, expect_status=404) == {'error': f'zone \'{id}\' does not exist'}
    zone_client.create(id)
    assert zone_client.update(id, zone) == zone
    assert zone_client.get(id) == zone
    zone_client.delete(id)
