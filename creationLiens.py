import json
import random


data = []


prenomPersonnes = ['noé', 'leo', 'lucie', 'paul', 'marie', 'jean', 'pierre', 'marc', 'luc', 'louis', 'jeanne', 'marcel', 'marcelle', 'marianne']


for people in prenomPersonnes:
    dataPersonne = {
        "name": people,
    }
    
    choice = prenomPersonnes.copy()
    choice.remove(people)

    # l'algo créé des liens entre les gens mais c'est obsolète
    # for i in range(0, random.randint(1, 9)):
    #     randomPersonne = random.choice(choice)
    #     choice.remove(randomPersonne)

    #     selectPersonne = {"name":randomPersonne, "score":random.randint(1, 100)}
    #     dataPersonne["friends"].append(selectPersonne)
    
    
    data.append(dataPersonne)

d = open('data.json', 'w', encoding='utf8')
d.write(json.dumps(data, indent=4, ensure_ascii=False))
