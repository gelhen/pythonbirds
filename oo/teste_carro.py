from unittest import TestCase

from pythonbirds.oo.carro import Motor


class CarroTestCase(TestCase):

    def setUp(self):
        self.motor = Motor()

    def teste_velocidade_inicial(self):
        self.assertEqual(0, self.motor.velocidade)

    def teste_acelerar(self):
        self.motor.acelerar()
        self.assertEqual(1, self.motor.velocidade)