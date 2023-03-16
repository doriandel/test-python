# --- PARTIE 2 ---
# Créer un script python qui va contenir un dictionnaire (par exemple une personne, avec des attributs comme l'âge, le prénom, le genre...)
# Retourner ce dictionnaire sous forme d'objet JSON dans le terminal (voir le package 'json' pour plus d'info)
# /!\ En POO également, vous devez initialiser le dictionnaire soit dans le constructeur soit avec un setter après instanciation de la classe /!\

import json

class Personne:
    def __init__(self, age, prenom, genre):
        self.age = age
        self.prenom = prenom
        self.genre = genre
    
    def to_json(self):
        return json.dumps({
            'age': self.age,
            'prenom': self.prenom,
            'genre': self.genre
        })

# initialiser le dictionnaire dans le constructeur
personne1 = Personne(age=30, prenom='Jean', genre='M')
print(personne1.to_json())

# initialiser le dictionnaire avec un setter après instanciation de la classe
personne2 = Personne(age=25, prenom='Marie', genre='F')
personne2.age = 27
personne2.genre = 'Autre'
print(personne2.to_json())
