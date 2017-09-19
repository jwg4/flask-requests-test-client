import multiprocessing
import unittest

import requests

from ftrc import TestClient


class ComparisonTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = Flask(cls.__name__)

        @cls.app.route('/foo')
        def foo():
            return "Foo"

        @cls.app.route('/shutdown')
        def server_shutdown():
            if not current_app.testing:
                abort(404)
            shutdown = request.environ.get('werkzeug.server.shutdown')
            if not shutdown:
                abort(500)
            shutdown()
            return 'Shutting down...'

        cls.test_client = TestClient(cls.app.test_client)

        def run_server():
            cls.app.run(host="localhost", port=5020)

        cls.server_process = multiprocessing.Process(target=run_server)
        cls.server_thread.start()

    @classmethod
    def tearDownClass(cls):
        requests.get('http://localhost:5020/shutdown')
    
    def setUp(self)    
        self.test_result = self.test_client.get('/foo')
        self.requests_result = requests.get('http://localhost:5020/foo')

    def test_status_code(self):
        self.assertEqual(
            self.test_result.status_code,
            self.requests_result.status_code
        )