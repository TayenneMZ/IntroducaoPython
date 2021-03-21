import Bolha
import random
import time

class ContaTempos:
    def lista_aleatoria(self, tamanho):
        #Para cada x ele vai calcular um número random inteiro
        lista = [random.randrange(1000) for x in range(tamanho)]
        return lista

    def lista_quase_ordenada(self, tamanho):
        #Cria uma lista que é 0, 1, 2, 3...
        lista = [x for x in range(tamanho)]
        lista[tamanho//10] = -500
        return lista
    
    def compara(self, tamanho):
        lista1 = self.lista_aleatoria(tamanho)
        lista2 = lista1[:]

        print("Comparando com listas aleatorias")
        
        o = Bolha.Ordenador()
        antes = time.time()
        o.bubblesort_short(lista1)
        depois = time.time()

        print("Método bubblesort demorou: ", depois-antes)

        antes = time.time()
        o.selectionsort(lista2)
        depois = time.time()

        print("Método selectionsort demorou: ", depois-antes)

        lista1 = self.lista_quase_ordenada(tamanho)
        lista2 = lista1[:]
        
        print("Comparando com listas quase ordenadas")
        
        o = Bolha.Ordenador()
        antes = time.time()
        o.bubblesort_short(lista1)
        depois = time.time()

        print("Método bubblesort demorou: ", depois-antes)

        antes = time.time()
        o.selectionsort(lista2)
        depois = time.time()

        print("Método selectionsort demorou: ", depois-antes)
        
