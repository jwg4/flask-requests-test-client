import logging
import threading
import time
import unittest

import requests
import flask

from frtc import TestClient

logging.getLogger('werkzeug').setLevel(logging.ERROR)


class ComparisonTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = flask.Flask(cls.__name__)

        @cls.app.route('/foo')
        def foo():
            return "Foo"

        @cls.app.route('/shutdown')
        def server_shutdown():
            shutdown = flask.request.environ.get('werkzeug.server.shutdown')
            if not shutdown:
                flask.abort(500)
            shutdown()
            return 'Shutting down...'

        cls.test_client = TestClient(cls.app.test_client())

        def run_server():
            cls.app.run(host="localhost", port=5020)

        cls.server_thread = threading.Thread(target=run_server)
        cls.server_thread.start()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        requests.get('http://localhost:5020/shutdown')

    def setUp(self):
        self.test_result = self.test_client.get('/foo')
        self.requests_result = requests.get('http://localhost:5020/foo')

    def check_property(self, field_name):
        self.assertEqual(
            getattr(self.test_result, field_name),
            getattr(self.requests_result, field_name)
        )

    def test_status_code(self):
        self.check_property('status_code')

    def test_apparent_encoding(self):
        self.check_property('apparent_encoding')

    def test_encoding(self):
        self.check_property('encoding')

    def test_text(self):
        self.check_property('text')

    @unittest.skip("Currently the test server and debug server do not serve the same headers.")
    def test_headers(self):
        self.check_property('headers')
