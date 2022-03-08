from uuid import uuid4


def test_create_delete_zone(client):
    zone = uuid4()

    response = client.get(f'/v1/zones/{zone}')
    assert response.status_code == 404
    assert response.json == {'error': f'zone \'{zone}\' does not exist'}

    response = client.post(f'/v1/zones/{zone}')
    assert response.status_code == 200
    assert response.json == {'groups': []}

    response = client.get(f'/v1/zones/{zone}')
    assert response.status_code == 200
    assert response.json == {'groups': []}

    response = client.delete(f'/v1/zones/{zone}')
    assert response.status_code == 200
    assert response.json == {'message': f'successfully deleted zone \'{zone}\''}

    response = client.get(f'/v1/zones/{zone}')
    assert response.status_code == 404
    assert response.json == {'error': f'zone \'{zone}\' does not exist'}
