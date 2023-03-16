# --- PARTIE 1 ---
# Créer un script python qui va afficher dans le terminal une phrase aléatoire,
# venant d'un tableau que vous aurez préalablement rempli de quelques citations par exemple
# /!\ En POO même s'il y a peu d'attributs/getters/setters à faire /!\

import random

class PhraseAleatoire:
    def __init__(self, citations):
        self.citations = citations
    
    def generer(self):
        return random.choice(self.citations)

citations = [
    "Le chemin de mille lieues commence par un pas. - Lao Tseu",
    "La vie est un mystère qu'il faut vivre, et non un problème à résoudre. - Gandhi",
    "Soyez le changement que vous voulez voir dans le monde. - Gandhi",
    "La vie est un défi à relever, un bonheur à mériter, une aventure à tenter. - Mère Teresa"
]

phrase_aleatoire = PhraseAleatoire(citations)
print(phrase_aleatoire.generer())

