import csv
import json
nom = []
with open('dataSet/patronymes.csv', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        try:
            if int(row[1]) >= 1000:
                nom.append(row[0])
        except:
            print('il y a eu une erreur à la ligne : ', row)

file = open('nom.json', 'w', encoding='utf8')
file.write(json.dumps(nom, indent=4, ensure_ascii=False))
file.close()