from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):
    def test_a(self):
        with patch("requests.get") as g:
            with patch("requests.post") as p:
                g.return_value.text = "Cal Kestis Coruscant"
                p.return_value.text = "Home of The Senate"
                response = self.client.get(url_for('index'))
                self.assertIn(b'Cal Kestis Coruscant', response.data)
                self.assertIn(b'Home of The Senate', response.data)