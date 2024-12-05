from input import memoria_corrompida
import re

def soma_multiplicacoes_habilitadas(memoria_corrompida):

    padrao_mul = r'mul\((\d+),(\d+)\)' 
    padrao_do_dont = r'(do\(\)|don\'t\(\))'

    partes = re.findall(f'{padrao_do_dont}|{padrao_mul}', memoria_corrompida)
    
    habilitado = True 
    soma = 0

    for parte in partes:
        if parte[0] == "do()":
            habilitado = True
        elif parte[0] == "don't()":
            habilitado = False
        elif parte[1].isdigit() and parte[2].isdigit():
            a, b = int(parte[1]), int(parte[2])
            if habilitado:
                soma += a * b

    return soma

resultado = soma_multiplicacoes_habilitadas(memoria_corrompida)
print(f"Resultado: {resultado}")
