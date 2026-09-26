import requests

def buscar_dados(url):
    resposta = requests.get(url)
    return resposta.json()

def calcular_maior(dados):
    maior = 0.0

    for registro in dados:
        valor = float(registro['valor'])
        if  valor > maior:
            maior = valor
    return maior

def main():
    url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados?formato=json&dataInicial=01/09/2026&dataFinal=25/09/2026'
    dados = buscar_dados(url)
    resultado = calcular_maior(dados)
    print(f'Maior Valor Encontrado: {resultado}')
main()