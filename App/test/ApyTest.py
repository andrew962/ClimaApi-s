import unittest

from App.api import estatus
from App.api import hume
from App.api import lugar
from App.api import tempe,tempe1,tempe2
from App.api import viento


class ClimaTest(unittest.TestCase):
    def test_estatus(self):
        self.assertEquals(estatus,'Clear')

    def test_lugar(self):
        self.assertEquals(lugar,'AR')

    def test_tempe(self):
        self.assertEquals(tempe,16.06)

    def test_tempe1(self):
        self.assertEquals(tempe1,18.0)

    def test_tempe2(self):
        self.assertEquals(tempe2,14.0)

    def test_viento(self):
        self.assertEquals(viento,2.6)

    def test_humedad(self):
        self.assertEquals(hume,87)