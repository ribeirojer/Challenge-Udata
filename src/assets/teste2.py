import csv

with open('dados_sem_formatacao.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter='+')
    header = next(reader)  # lê a primeira linha e armazena como cabeçalho
    # lê as linhas restantes e armazena como dados
    data = [row for row in reader]

result = []
for row in data:
    result.append(dict(zip(header, row)))

print(result)
