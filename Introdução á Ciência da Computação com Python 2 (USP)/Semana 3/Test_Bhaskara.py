import Bhaskara
import pytest

class TestBhaskara:

    @pytest.fixture
    def b(self):
        return Bhaskara.Bhaskara()

    @pytest.mark.parametrize("entrada1, entrada2, entrada3, tamanho, saida", [
        (1, 0, 0, 1, (0)),
        (1, -5, 6, 2, (3, 2)),
        (10, 10, 10, 0, ()),
        (10, 20, 10, 1, (-1))
        ])
    
    def testa_raiz(self, b):
        assert b.calcula_raizes(entrada1, entrada2, entrada3) == (tamanho, saida)
