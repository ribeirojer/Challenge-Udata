import json
import csv

data = []
header = ['Ano', 'Mês', 'País Importado',
          'Produto', 'UF Importadora', 'Via', 'FOB (US$)']

with open('dados_sem_formatacao.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        new_row = row[0].split("+")
        if (new_row[4] == 'Santa Catarina'):
            data.append(new_row)

# Criar um dicionário para contar as importações por país
importacoes_por_pais = {}
for row in data:
    if row[0] == '2020' and row[4] == 'Santa Catarina':
        pais = row[2]
        valor = float(row[6])
        if pais in importacoes_por_pais:
            importacoes_por_pais[pais] += valor
        else:
            importacoes_por_pais[pais] = valor

# Ordenar os países por valor de importação
paises_ordenados = sorted(importacoes_por_pais.items(),
                          key=lambda x: x[1], reverse=True)

# Imprimir os 5 primeiros países
print("Os países que mais importaram para Santa Catarina em 2020 foram:")
for pais, valor in paises_ordenados:
    print(f"{pais}: US$ {valor:.2f}")

data.insert(0, header)
print(data[0:3])
print("Dados salvos com sucesso!")

# Dados a serem exportados
dados = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

with open("saida.json", "w", encoding="utf-8") as f:
    json.dump(paises_ordenados, f, ensure_ascii=False)

print("Arquivo exportado com sucesso!")
