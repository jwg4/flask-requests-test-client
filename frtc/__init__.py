class TestClient(object):
    def __init__(self, client):
        self.client = client
        
    def get(self, url):
        return Response(self.client.get(url))


class Response(object):
    def __init__(self, response):
        self.response = response

    @property
    def status_code(self):
        return self.response.status_code

    @property
    def apparent_encoding(self):
        return 'ascii'