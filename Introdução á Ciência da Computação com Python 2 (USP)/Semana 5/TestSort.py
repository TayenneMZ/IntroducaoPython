import Bolha
import ContaTempos
import pytest

class TestSort:
    @pytest.fixture
    def o(self):
        return Bolha.Ordenador()

    @pytest.fixture
    def l_almost(self):
        c = ContaTempos.ContaTempos()
        return c.lista_quase_ordenada(100)

    @pytest.fixture
    def l_random(self):
        c = ContaTempos.ContaTempos()
        return c.lista_aleatoria(100)

    def is_sort(self, array):
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                return False
        return True
                
            
    def test_bubblesort_short_random(self, o, l_random):
        o.bubblesort_short(l_random)
        assert self.is_sort(l_random)

    def test_selectionsort_random(self, o, l_random):
        o.bubblesort_short(l_random)
        assert self.is_sort(l_random)

    def test_bubblesort_short_almost(self, o, l_almost):
        o.bubblesort_short(l_almost)
        assert self.is_sort(l_almost)

    def test_selectionsort_almost(self, o, l_almost):
        o.bubblesort_short(l_almost)
        assert self.is_sort(l_almost)
