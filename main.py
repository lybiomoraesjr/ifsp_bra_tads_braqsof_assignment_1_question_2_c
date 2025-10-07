import unittest


def calcular_ir(base_calculo):
    """
    Calcula o Imposto de Renda com base em uma dada base de cálculo.
    """
    if not isinstance(base_calculo, (int, float)):
        return "Erro: Entrada deve ser numérica."
    if base_calculo < 0:
        return "Erro: Salário não pode ser negativo."
    if base_calculo <= 2259.20:
        imposto = 0.0
    elif base_calculo <= 2826.65:
        imposto = (base_calculo * 0.075) - 169.44
    elif base_calculo <= 3751.05:
        imposto = (base_calculo * 0.15) - 381.44
    elif base_calculo <= 4664.68:
        imposto = (base_calculo * 0.225) - 662.77
    else:
        imposto = (base_calculo * 0.275) - 896.00
    return imposto


class TestCalculoIRSeteCasos(unittest.TestCase):

    def test_CE1_salario_na_faixa_de_isencao(self):
        """Testa o caso CE1: Salário na faixa de isenção."""
        print("Executando: test_CE1_salario_na_faixa_de_isencao")
        self.assertAlmostEqual(calcular_ir(1500.00), 0.00, places=2)

    def test_CE2_salario_na_faixa_de_aliquota_7_5(self):
        """Testa o caso CE2: Salário na faixa de alíquota de 7,5%."""
        print("Executando: test_CE2_salario_na_faixa_de_aliquota_7_5")
        self.assertAlmostEqual(calcular_ir(2500.00), 18.06, places=2)

    def test_CE3_salario_na_faixa_de_aliquota_15(self):
        """Testa o caso CE3: Salário na faixa de alíquota de 15%."""
        print("Executando: test_CE3_salario_na_faixa_de_aliquota_15")
        self.assertAlmostEqual(calcular_ir(3000.00), 68.56, places=2)

    def test_CE4_salario_na_faixa_de_aliquota_22_5(self):
        """Testa o caso CE4: Salário na faixa de alíquota de 22,5%."""
        print("Executando: test_CE4_salario_na_faixa_de_aliquota_22_5")
        self.assertAlmostEqual(calcular_ir(4000.00), 237.23, places=2)

    def test_CE5_salario_na_faixa_de_aliquota_27_5(self):
        """Testa o caso CE5: Salário na faixa de alíquota de 27,5%."""
        print("Executando: test_CE5_salario_na_faixa_de_aliquota_27_5")
        self.assertAlmostEqual(calcular_ir(5000.00), 479.00, places=2)

    def test_CI1_salario_com_valor_negativo(self):
        """Testa o caso CI1: Salário com valor negativo."""
        print("Executando: test_CI1_salario_com_valor_negativo")
        self.assertEqual(calcular_ir(-100.00), "Erro: Salário não pode ser negativo.")

    def test_CI2_entrada_com_valor_nao_numerico(self):
        """Testa o caso CI2: Entrada com valor não numérico."""
        print("Executando: test_CI2_entrada_com_valor_nao_numerico")
        self.assertEqual(calcular_ir("abc"), "Erro: Entrada deve ser numérica.")


if __name__ == '__main__':
    unittest.main(verbosity=2)