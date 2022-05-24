from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app



class TestBase(TestCase):
    def create_app(self):
        return app

class TestPlanet(TestBase):
    def test_fcoruscant(self):
        with patch('random.randint') as r:
            r.return_value = 0
            response = self.client.get(url_for('planet'))
            self.assertIn(b'Tatooine', response.data)

class TestPlanet(TestBase):
    def test_gkashyyyk(self):
        with patch('random.randint') as r:
            r.return_value = 1
            response = self.client.get(url_for('planet'))
            self.assertIn(b'Coruscant', response.data)

    def test_hshilli(self):
        with patch('random.randint') as r:
            r.return_value = 2
            response = self.client.get(url_for('planet'))
            self.assertIn(b'Kamino', response.data)


    def test_ikamino(self):
        with patch('random.randint') as r:
            r.return_value = 3
            response = self.client.get(url_for('planet'))
            self.assertIn(b'Ryloth', response.data)

    def test_jryloth(self):
        with patch('random.randint') as r:
            r.return_value = 4
            response = self.client.get(url_for('planet'))
            self.assertIn(b'Shili', response.data)
