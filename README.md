# Flask Requests Test Client

This package is an alternative to the flask test client, one which has a very similar interface to the *requests* package. This allows the same tests to be re-used against the test client (using this package) and an actual HTTP server (using requests).

```
>>> from flask import Flask
>>> app = Flask(__name__)

>>> @app.route('/hello')
... def hello_world():
...     return jsonify({'msg': 'Hello, World!'})

>>> from frtc import TestClient
>>> client = TestClient(app.test_client)

>>> r = client.get('/hello')
>>> r.status_code
200
>>> r.headers['content-type']
'application/json; charset=utf8'
>>> r.encoding
'utf-8'
>>> r.text
u'{"msg":"Hello, World!"}'
>>> r.json()
{u'msg': u'Hello, World!'}

```