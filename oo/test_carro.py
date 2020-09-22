from unittest import TestCase

from oo.Carro import Motor

class CarroTestCase(TestCase):#Click Menos Usado Aqui -> Roda todos os Testes DEFs Da Classe:
    def test_velocidade_inicial(self):
        motor = Motor() #Motod com M Maiusculo é a Classe Motor que tem 3 DEFs
        self.assertEqual(0, motor.velocidade) #Ou -> A velocidade tem que ser == 0

    def teste_acelerar(self): #Clicando com o MenosUsado Aqui -> Roda só este Teste:
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)

"""
Para Fazer o Teste com sucesso:
Cliquei em 'Terminal' (No Pycharm), e usei as teclas (Ctr Shift Enter).
Só assim o teste funcionou.
"""


