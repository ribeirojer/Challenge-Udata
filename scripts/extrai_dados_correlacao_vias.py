import csv
import json
from collections import defaultdict


def calculate_std_dev(arr):
    n = len(arr)
    mean = sum(arr) / n
    variance = sum((x - mean) ** 2 for x in arr) / (n - 1)
    std_dev = variance ** 0.5
    return std_dev


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

maritima = [row[1] for row in result_sorted[1:]]
rodoviaria = [row[2] for row in result_sorted[1:]]
aerea = [row[3] for row in result_sorted[1:]]

saida = [calculate_std_dev(maritima), calculate_std_dev(
    rodoviaria), calculate_std_dev(aerea)]

with open("desvio_vias.json", "w", encoding="utf-8") as f:
    json.dump(saida, f, ensure_ascii=False)
