
from input import entrada

def pontuacao_similaridade(esquerda, direita):
    pontuacao = 0
    for num in esquerda:
        frequencia = direita.count(num)
        pontuacao += num * frequencia
    return pontuacao

linhas = entrada.strip().split("\n")
esquerda_lista = []
direita_lista = []

for linha in linhas:
    num1, num2 = map(int, linha.split())
    esquerda_lista.append(num1)
    direita_lista.append(num2)

resultado = pontuacao_similaridade(esquerda_lista, direita_lista)
print("A distância total é:", resultado)
