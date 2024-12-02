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

def relatorio_seguro_com_remocao(niveis):
    if relatorio_seguro(niveis):
        return True 
    
    for i in range(len(niveis)):
        niveis_modificados = niveis[:i] + niveis[i+1:]
        if relatorio_seguro(niveis_modificados):
            return True
    
    return False

linhas = dados.strip().split("\n")
quantidade_segura = 0

for linha in linhas:
    niveis = list(map(int, linha.split()))
    if relatorio_seguro_com_remocao(niveis):
        quantidade_segura += 1

print("Quantidade de relatórios seguros:", quantidade_segura)