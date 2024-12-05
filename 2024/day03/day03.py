from input import memoria_corrompida
import re

def soma_multiplicacoes(memoria_corrompida):

    padrao = r'mul\((\d+),(\d+)\)'

    instrucoes = re.findall(padrao, memoria_corrompida)
    
    soma = sum(int(x) * int(y) for x, y in instrucoes)
    
    return soma

resultado = soma_multiplicacoes(memoria_corrompida)
print("A soma das multiplicações válidas é:", resultado)
