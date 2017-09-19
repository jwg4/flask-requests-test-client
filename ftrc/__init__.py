class TestClient(object):
    def __init__(self, client):
        self.client = client
        
    def get(self, url):
        return self.client.get(url)