
from input import entrada

def distancia_total(esquerda, direita):
    esquerda.sort()
    direita.sort()
    return sum(abs(l - r) for l, r in zip(esquerda, direita))

linhas = entrada.strip().split("\n")
esquerda_lista = []
direita_lista = []

for linha in linhas:
    num1, num2 = map(int, linha.split())
    esquerda_lista.append(num1)
    direita_lista.append(num2)

resultado = distancia_total(esquerda_lista, direita_lista)
print("A distância total é:", resultado)
