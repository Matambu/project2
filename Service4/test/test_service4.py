from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestDatabank(TestBase):
    def test_k(self):
        response = self.client.post(url_for('databank'), data = 'Coruscant-Cal Kestis')
        self.assertIn(b'Home of Senate', response.data)

    def test_l(self):
        response = self.client.post(url_for('databank'), data = 'Tatooine-Cal Kestis')
        self.assertIn(b'Home of Cal Kestis', response.data)
    
    def test_m(self):
        response = self.client.post(url_for('databank'), data = 'Kamino-Cal Kestis')
        self.assertIn(b'Home of Clones', response.data)
    
    def test_n(self):
        response = self.client.post(url_for('databank'), data = 'Ryloth-Cal Kestis')
        self.assertIn(b'Home of Twilek', response.data)
    
    def test_o(self):
        response = self.client.post(url_for('databank'), data = 'Shili-Cal Kestis')
        self.assertIn(b'Home of Ahsoka', response.data)

    def test_p(self):
        response = self.client.post(url_for('databank'), data = 'Shili-Ahsoka Tano')
        self.assertIn(b'Home of Ahsoka', response.data)
    
    def test_q(self):
        response = self.client.post(url_for('databank'), data = 'Tatooine-Ahsoka Tano')
        self.assertIn(b'Home of The Skywalker', response.data)
    
    def test_r(self):
        response = self.client.post(url_for('databank'), data = 'Coruscant-Ahsoka Tano')
        self.assertIn(b'Home of The Senate', response.data)

    def test_u(self):
        response = self.client.post(url_for('databank'), data = 'Kamino-Grand Inquisitor')
        self.assertIn(b'Home of The Clones', response.data)
    
    def test_v(self):
        response = self.client.post(url_for('databank'), data = 'Tatooine-Grand Inquisitor')
        self.assertIn(b'Home of The Skywalker', response.data)

    def test_w(self):
        response = self.client.post(url_for('databank'), data = 'Coruscant-Grand Inquisitor')
        self.assertIn(b'Home of The Senate', response.data)

    def test_x(self):
        response = self.client.post(url_for('databank'), data = 'Ryloth-Grand Inquisitor')
        self.assertIn(b'Home of The Twilek', response.data)

    def test_y(self):
        response = self.client.post(url_for('databank'), data = 'Shili-Grand Inquisitor')
        self.assertIn(b'Home of Ahsoka', response.data)

    def databank_10(self):
        response = self.client.post(url_for('databank', data = 'Shili-Kylo Ren'))
        self.assertIn(b'Home of Ahsoka', response.data)
    
    
    
    def databank_10(self):
        response = self.client.post(url_for('databank'), data = 'Shili-Kylo Ren')
        self.assertIn(b'Home of Ahsoka', response.data)

    def databank_11(self):
        response = self.client.post(url_for('databank'), data = 'Tatooine-Kylo Ren')
        self.assertIn(b'Home of Uncle', response.data)
    
    def databank_12(self):
        response = self.client.post(url_for('databank'), data = 'Coruscant-Kylo Ren')
        self.assertIn(b'Home of The Senate', response.data)
    
    def databank_13(self):
        response = self.client.post(url_for('databank'), data = 'Kamino-Kylo Ren')
        self.assertIn(b'Home of The Clones', response.data)

    def databank_14(self):
        response = self.client.post(url_for('databank'), data = 'Tatooine-Shaak-Ti')
        self.assertIn(b'Home of Skywalker', response.data)
    
    def databank_j(self):
        response = self.client.post(url_for('databank'), data = 'Coruscant-Shaak-Ti')
        self.assertIn(b'Home of Senate', response.data)
    
    def databank_16(self):
        response = self.client.post(url_for('databank'), data = 'Kamino-Shaak-Ti')
        self.assertIn(b'Home of Clones', response.data)
    
    def databank_17(self):
        response = self.client.post(url_for('databank'), data = 'Ryloth-Shaak-Ti')
        self.assertIn(b'Home of Twilek', response.data)

    def databank_9(self):
        response = self.client.post(url_for('databank'), data = 'Shili-Shaak-Ti')
        self.assertIn(b'Home of Twilek', response.data)
    

    