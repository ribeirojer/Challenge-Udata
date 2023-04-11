import csv
import json

def correlation(x, y):
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    std_x = sum((xi - mean_x)**2 for xi in x) / (n - 1)
    std_y = sum((yi - mean_y)**2 for yi in y) / (n - 1)
    cov = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y)) / (n - 1)
    return cov / (std_x * std_y)

with open("dados_formatados.csv", 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    produtos = {}
    for row in reader:
        produto = row['Produto']
        fob = int(row['FOB (US$)'])
        if produto in produtos:
            produtos[produto]['quantidade'] += 1
            produtos[produto]['fob_total'] += fob
        else:
            produtos[produto] = {'quantidade': 1, 'fob_total': fob}

produtos_array = [[produto, info['quantidade'], info['fob_total']]
                  for produto, info in produtos.items()]

quantidades = []
fobs = []
for produto, quantidade, fob_total in produtos_array:
    quantidades.append(quantidade)
    fobs.append(fob_total)
    print(
        f'O produto "{produto}" foi exportado {quantidade} vezes, com um FOB total de {fob_total} dólares.')

print("Quantidades:", quantidades)
print("FOBs:", fobs)
print("Quantidades:", len(quantidades))
print("FOBs:", len(fobs))

print(correlation(quantidades, fobs))
with open("correlacao.json", "w", encoding="utf-8") as f:
    json.dump(produtos_array, f, ensure_ascii=False)
