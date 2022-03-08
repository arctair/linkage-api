class ZoneClient:
    def __init__(self, client):
        self.client = client

    def get(self, id: str, expect_status: int = 200) -> dict:
        response = self.client.get(f'/v1/zones/{id}')
        assert response.status_code == expect_status
        return response.json

    def create(self, id: str, expect_status: int = 200) -> dict:
        response = self.client.post(f'/v1/zones/{id}')
        assert response.status_code == expect_status
        return response.json

    def delete(self, id: str, expect_status: int = 200) -> dict:
        response = self.client.delete(f'/v1/zones/{id}')
        assert response.status_code == expect_status
        return response.json

    def update(self, id: str, zone: dict, expect_status: int = 200) -> dict:
        response = self.client.put(f'/v1/zones/{id}', json=zone)
        assert response.status_code == expect_status
        return response.json
