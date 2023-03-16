# --- PARTIE 3 ---
# Créer un script python qui va récupérer les informations systèmes (voir les packages 'platform', 'cpuinfo', 'socket' et 'os' pour plus d'info)
# Avec le moteur de templating jinja, afficher dans un beau template HTML (avec du CSS dans un fichier CSS séparé) ces informations systèmes
# Évidemment, le tout en POO...
# /!\ Je demande pas le site de l'année, mais faites un effort sur le CSS svp /!\

import platform
import cpuinfo
import socket
import os
from jinja2 import Environment, FileSystemLoader

# Récupérer les infos
systeme = platform.system()
processeur = cpuinfo.get_cpu_info()['brand']
nom_hote = socket.gethostname()
adresse_ip = socket.gethostbyname(nom_hote)
repertoire_courant = os.getcwd()

# Créer un env Jinja2 et loader le template HTML
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

# Rendu du template
html = template.render(systeme=systeme, processeur=processeur, nom_hote=nom_hote, adresse_ip=adresse_ip, repertoire_courant=repertoire_courant)

# Enregistrer le HTML dans un fichier
with open('informations_systeme.html', 'w') as f:
    f.write(html)
