import csv
import json

data = []
total = {"MARITIMA": {}, "RODOVIARIA": {}, "AEREA": {}, "ENTRADA/SAIDA FICTA": {}, "MEIOS PROPRIOS": {}, "POSTAL": {}}

with open("dados_formatados.csv", 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

data.pop(0)


for row in data:
    month = row[0]
    via = row[3]
    fob = int(row[4])
    
    if via == 'MARITIMA':
        if month not in total['MARITIMA']:
            total['MARITIMA'][month] = fob
        else:
            total['MARITIMA'][month] += fob
    if via == 'RODOVIARIA':
        if month not in total["RODOVIARIA"]:
            total["RODOVIARIA"][month] = fob
        else:
            total["RODOVIARIA"][month] += fob
    if via == 'AEREA':
        if month not in total["AEREA"]:
            total["AEREA"][month] = fob
        else:
            total["AEREA"][month] += fob
    if via == 'ENTRADA/SAIDA FICTA':
        if month not in total["ENTRADA/SAIDA FICTA"]:
            total["ENTRADA/SAIDA FICTA"][month] = fob
        else:
            total["ENTRADA/SAIDA FICTA"][month] += fob
    if via == 'MEIOS PROPRIOS':
        if month not in total["MEIOS PROPRIOS"]:
            total["MEIOS PROPRIOS"][month] = fob
        else:
            total["MEIOS PROPRIOS"][month] += fob
    if via == 'POSTAL':
        if month not in total["POSTAL"]:
            total["POSTAL"][month] = fob
        else:
            total["POSTAL"][month] += fob

months = {}
for key, value in total.items():
    months.update(value)

transport_modes = list(total.keys())

result = [["Mês"] + transport_modes + ["Média"]]

for month in sorted(months.keys()):
    row = [month]
    values = []
    for transport_mode in transport_modes:
        value = total.get(transport_mode, {}).get(month, 0)
        row.append(value)
        values.append(value)
    average = sum(values) / len(values)
    row.append(average)
    result.append(row)

# Exibe o resultado
for row in result:
    print(row)

with open("vias_por_mes_array.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False)
