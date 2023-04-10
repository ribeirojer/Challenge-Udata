import csv
import json
from collections import defaultdict

total = defaultdict(dict)
transport_modes = ["MARITIMA", "RODOVIARIA", "AEREA",
                   "ENTRADA/SAIDA FICTA", "MEIOS PROPRIOS", "POSTAL"]

with open("dados_formatados.csv", 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # skip header row
    for row in reader:
        month, _, _, via, fob = row
        fob = int(fob)
        total[via][month] = total[via].get(month, 0) + fob

result = [["Mês"] + transport_modes + ["Média"]]
for month in sorted(total['MARITIMA'].keys()):
    row = [month]
    values = []
    for transport_mode in transport_modes:
        value = total[transport_mode].get(month, 0)
        row.append(value)
        values.append(value)
    average = sum(values) / len(values)
    row.append(average)
    result.append(row)

result_sorted = sorted(result[1:], key=lambda x: int(x[0]))
result_sorted.insert(0, result[0])

for row in result_sorted:
    print(row)

with open("vias_por_mes_array2.json", "w", encoding="utf-8") as f:
    json.dump(result_sorted, f, ensure_ascii=False)
