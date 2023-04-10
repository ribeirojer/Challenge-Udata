import csv

data = []
header = ['Mês', 'País Importado',
          'Produto', 'Via', 'FOB (US$)']

with open('dados_sem_formatacao.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        new_row = row[0].split("+")
        if (new_row[4] == 'Santa Catarina'):
            data.append(new_row[1:4]+new_row[5:])

data.insert(0, header)

with open('dados_formatados.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Escrever os dados no arquivo CSV
    writer.writerows(data)
