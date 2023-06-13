import json
import random


# Création des personnes

noms = json.load(open('data/nom.json', 'r', encoding='utf8'))
prenoms = json.load(open('data/prenom.json', 'r', encoding='utf8'))

data = []

print(len(prenoms))

for prenom in prenoms:
    nbPersonne = random.randint(1, len(noms))
    for x in range(nbPersonne):
        nom = random.choice(noms)
        data.append({
            "prenom": prenom,
            "nom": nom,
            'id': prenom[0] + nom.lower().replace(' ', '_') + str(random.randint(1, 1000000))
        })

d = open('data/data.json', 'w', encoding='utf8')
d.write(json.dumps(data, indent=4, ensure_ascii=False))

"""

Création des liens

data = json.load(open('data.json', encoding='utf8'))

finalData = []

for personne in data:
    nbLiens = random.randint(10, 35)
    liens = []
    for x in range(nbLiens):
      choix = random.choice(data)
      if choix["id"] not in liens:
        liens.append(id)
        finalData.append({
            1 : personne["id"],
            2 : choix["id"]
        })

d = open('dataFinal.json', 'w', encoding='utf8')
d.write(json.dumps(finalData, indent=4, ensure_ascii=False))

"""