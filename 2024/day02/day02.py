from input import dados

def relatorio_seguro(niveis):
    crescente = True
    decrescente = True
    
    for i in range(len(niveis) - 1):
        diferenca = niveis[i + 1] - niveis[i]
        if not (1 <= abs(diferenca) <= 3): 
            return False
        if diferenca < 0:
            crescente = False
        if diferenca > 0: 
            decrescente = False
    
    return crescente or decrescente 

linhas = dados.strip().split("\n")
quantidade_segura = 0

for linha in linhas:
    niveis = list(map(int, linha.split()))
    if relatorio_seguro(niveis):
        quantidade_segura += 1

print("Quantidade de relatórios seguros:", quantidade_segura)