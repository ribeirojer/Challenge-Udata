import csv
import json

def rename_country(country_name):
    country_name = country_name.lower()
    country_dict = {
        'brasil': 'brazil',
        'argentina': 'argentina',
        'uruguai': 'uruguay',
        'paraguai': 'paraguay',
        'estados unidos': 'united states',
        'canadá': 'canada',
        'méxico': 'mexico',
        'espanha': 'spain',
        'frança': 'france',
        'alemanha': 'germany',
        'itália': 'italy',
        'reino unido': 'united kingdom',
        'japão': 'japan',
        'china': 'china',
        'coréia do sul': 'south korea',
        'índia': 'india',
        'austrália': 'australia',
        'nova zelândia': 'new zealand',
        'egito': 'egypt',
        'equador': 'ecuador',
        'nigéria': 'nigeria',
        'venezuela': 'venezuela',
        'noruega': 'norway',
        'paquistão': 'pakistan',
        'irlanda': 'ireland',
        'dinamarca': 'denmark',
        'sri lanka': 'sri lanka',
        'eslováquia': 'slovakia',
        'romênia': 'romania',
        'argélia': 'algeria',
        'emirados árabes unidos': 'united arab emirates',
        'filipinas': 'philippines',
        'guiana': 'guyana',
        'tunísia': 'tunisia',
        'costa rica': 'costa rica',
        'guatemala': 'guatemala',
        'eslovênia': 'slovenia',
        'ucrânia': 'ukraine',
        'bolívia': 'bolivia',
        'cazaquistão': 'kazakhstan',
        'el salvador': 'el salvador',
        'bielorrússia': 'belarus',
        'porto rico': 'puerto rico',
        'macedônia do norte': 'north macedonia',
        'república do congo': 'republic of the congo',
        'estônia': 'estonia',
        'malta': 'malta',
        'bulgária': 'bulgaria',
        'letônia': 'latvia',
        'nova caledônia': 'new caledonia',
        'camboja': 'cambodia',
        'luxemburgo': 'luxembourg',
        'lituânia': 'lithuania',
        'mianmar': 'myanmar',
        'grécia': 'greece',
        'panamá': 'panama',
        'uzbequistão': 'uzbekistan',
        'zâmbia': 'zambia',
        'ilhas do pacífico': 'pacific islands',
        'turcomenistão': 'turkmenistan',
        'liechtenstein': 'liechtenstein',
        'macau': 'macau',
        'sérvia': 'serbia',
        'albânia': 'albania',
        'geórgia': 'georgia',
        'palestina': 'palestine',
        'bósnia e herzegovina': 'bosnia',
        'Palestina': 'Palestine', 'Bósnia': 'bosnia',
        'Honduras': 'Honduras',
        'Chipre': 'Cyprus',
        'San': 'San',
        'Gana': 'Ghana',
        'Mongólia': 'Mongolia',
        'Croácia': 'Croatia',
        'Líbano': 'Lebanon',
        'Moldávia': 'Moldavia',
        'Samoa': 'samoa',
        'Anguilla': 'Anguilla',
        'Haiti': 'Haiti',
        'Nicarágua': 'Nicaragua',
        'Senegal': 'Senegal',
        'Virgens': 'virgins',
        'Cocos': 'coconuts',
        'Coveite': 'Coveitis',
        'Madagascar': 'Madagascar',
        'Fiji': 'fiji',
        'Zimbábue': 'Zimbabwe',
        'Trinidad': 'Trinidad',
        'Azerbaijão': 'Azerbaijan',
        'Bouvet': 'bouvet',
        'Afeganistão': 'Afghanistan',
        'Saara': 'sahara',
        'Bonaire': 'bonaire',
        'Islândia': 'Iceland',
        'Nepal': 'Nepal',
        'Santa': 'Santa',
        'Belize': 'Belize',
        'Somália': 'Somalia',
        'Virgens': 'virgins',
        'Quênia': 'Kenya',
        'Nauru': 'nauru',
        'Jersey': 'Jersey',
        'Uganda': 'Uganda',
        'Seicheles': 'Seychelles',
        'Jamaica': 'Jamaica',
        'Geórgia': 'Georgia',
        'Camarões': 'Cameroon',
        'Serra': 'Mountain range',
        'Etiópia': 'Ethiopia',
        'Gâmbia': 'Gambia',
        'Barbados': 'barbados',
        'Tonga': 'Tonga',
        'Cabo Verde': 'Cape Green',
        'Namíbia': 'namibia',
        'Niue': 'niue',
        'Christmas': 'christmas',
        'Armênia': 'Armenia',
        'Vanuatu': 'vanuatu',
        'Burundi': 'Burundi',
    }
    return country_dict.get(country_name, country_name)

data = []
importacoes_por_pais = {}

with open("dados_formatados.csv", 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

data.pop(0)

for row in data:
    #pais = row[3]
    pais = rename_country(row[2]).capitalize()
    valor = float(row[4])
    if pais in importacoes_por_pais:
        importacoes_por_pais[pais] += valor
    else:
        importacoes_por_pais[pais] = valor

paises_ordenados = sorted(importacoes_por_pais.items(),
                          key=lambda x: x[1], reverse=True)

#with open("os_20_paises.json", "w", encoding="utf-8") as f:
with open("os_20_produtos.json", "w", encoding="utf-8") as f:
    json.dump(paises_ordenados[0:20], f, ensure_ascii=False)
