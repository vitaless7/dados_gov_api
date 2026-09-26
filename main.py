import requests
url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados?formato=json&dataInicial=01/09/2026&dataFinal=25/09/2026'
resposta = requests.get(url)
dados = resposta.json()
print(dados[0]['valor'])
maior = 0.0
for registro in dados:
    valor = float(registro['valor'])
    if valor > maior:
        maior = valor
print(f'Maior Valor:{maior}')
