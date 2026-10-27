
import unittest

from financeiro import calcular_saldo


class TestCalcularSaldo(unittest.TestCase):

    def test_saldo_com_receitas_e_despesas(self):
        transacoes = [
            {"valor": 2000, "tipo": "receita"},
            {"valor": 150, "tipo": "despesa"},
            {"valor": 300, "tipo": "receita"},
        ]

        resultado = calcular_saldo(transacoes)

        self.assertEqual(resultado, 2150)

    def test_lista_vazia(self):
        transacoes = []

        resultado = calcular_saldo(transacoes)

        self.assertEqual(resultado, 0)


if __name__ == "__main__":
    unittest.main()



    def test_somente_receitas(self):
        transacoes = [
            {"valor": 1000, "tipo": "receita"},
            {"valor": 500, "tipo": "receita"},
        ]

        resultado = calcular_saldo(transacoes)

        self.assertEqual(resultado, 1500)

    def test_somente_despesas(self):
        transacoes = [
            {"valor": 100, "tipo": "despesa"},
            {"valor": 50, "tipo": "despesa"},
        ]

        resultado = calcular_saldo(transacoes)

        self.assertEqual(resultado, -150)
