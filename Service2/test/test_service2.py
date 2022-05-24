from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app



class TestBase(TestCase):
    def create_app(self):
        return app

class TestName(TestBase):
    def test_bcal_kestis(self):
        with patch('random.randint') as r:
            r.return_value = 0
            response = self.client.get(url_for('name'))
            self.assertIn(b'Cal Kestis', response.data)

    def test_cahsoka_tano(self):
        with patch('random.randint') as r:
            r.return_value = 1
            response = self.client.get(url_for('name'))
            self.assertIn(b'Kylo Ren', response.data)

    def test_dshaak_Ti(self):
        with patch('random.randint') as r:
            r.return_value = 2
            response = self.client.get(url_for('name'))
            self.assertIn(b'Grand Inquisitor', response.data)


    def test_egrandinquisitor(self):
        with patch('random.randint') as r:
            r.return_value = 3
            response = self.client.get(url_for('name'))
            self.assertIn(b'Ahsoka Tano', response.data)