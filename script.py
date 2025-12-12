import psutil
import socket
import platform
import datetime
import time
import os

def nb_coeur():
    return psutil.cpu_count(logical=True)

def frequence_cpu():
    return psutil.cpu_freq().current

def pourcentage_utilisation_cpu():
    return psutil.cpu_percent(interval=1)

def ram_utilisee():
    return psutil.virtual_memory().used / (1024 ** 3)

def ram_totale(): 
    return psutil.virtual_memory().total / (1024 ** 3)

def pourcentage_utilisation_ram():
    return psutil.virtual_memory().percent

def nom_machine():   
    return socket.gethostname()

def systeme_exploitation():   
    return f"{platform.system()} {platform.release()}"

def heure_demarrage():     
    boot_time = psutil.boot_time()
    return datetime.datetime.fromtimestamp(boot_time).strftime("%Y-%m-%d %H:%M:%S")

def temps_ecoule_depuis_demarrage():  
    boot_time = psutil.boot_time()
    return time.time() - boot_time

def nombre_utilisateurs_connectes():
    return len(psutil.users())

def adresse_ip_principale():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

def liste_processus_cpu():    
    processus_cpu = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        processus_cpu.append((proc.info['pid'], proc.info['name'], proc.info['cpu_percent']))
    return processus_cpu

def liste_processus_ram():    
    processus_ram = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
        processus_ram.append((proc.info['pid'], proc.info['name'], proc.info['memory_percent']))
    return processus_ram

def top_3_processus_gourmands():
    processus_dict = {}
    
    for proc in psutil.process_iter(['name', 'memory_percent']):
        nom = proc.info['name']
        cpu = proc.cpu_percent(interval=0.1)
        mem = proc.info['memory_percent']
        
        if cpu is not None and mem is not None:
            if nom in processus_dict:
                processus_dict[nom]['cpu'] += cpu
                processus_dict[nom]['mem'] += mem
            else:
                processus_dict[nom] = {'cpu': cpu, 'mem': mem}
    processus = []
    for nom, valeurs in processus_dict.items():
        processus.append([nom, valeurs['cpu'], valeurs['mem']])
    
    processus.sort(key=lambda x: (x[1], x[2]), reverse=True)
    
    resultat = ""
    for i in range(3):
        if i < len(processus):
            nom = processus[i][0]
            cpu = round(processus[i][1], 1)
            mem = round(processus[i][2], 1)
            resultat += f"{nom} - CPU: {cpu}% - RAM: {mem}%\n"
    
    return resultat


def stats_fichiers():
    stats = {
        'nb_txt': 0,
        'nb_pdf': 0,
        'nb_images': 0,
        'nb_videos': 0,
        'nb_audio': 0,
        'nb_total': 0,
        'taille_txt': 0,
        'taille_pdf': 0,
        'taille_images': 0,
        'taille_videos': 0,
        'taille_audio': 0,
        'taille_totale': 0
    }
    
    extensions_images = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg']
    extensions_videos = ['.mp4', '.avi', '.mkv', '.mov', '.wmv']
    extensions_audio = ['.mp3', '.wav', '.flac', '.ogg', '.m4a']
    
    # Parcourir tous les fichiers
    for root, dirs, files in os.walk('/home'):
        for fichier in files:
            chemin_complet = os.path.join(root, fichier)
            
            # Vérifier que le fichier existe et est accessible
            if os.path.isfile(chemin_complet):
                extension = os.path.splitext(fichier)[1].lower()
                
                # Récupérer la taille
                taille = os.path.getsize(chemin_complet)
                stats['nb_total'] += 1
                stats['taille_totale'] += taille
                
                # Compter par type
                if extension == '.txt':
                    stats['nb_txt'] += 1
                    stats['taille_txt'] += taille
                elif extension == '.pdf':
                    stats['nb_pdf'] += 1
                    stats['taille_pdf'] += taille
                elif extension in extensions_images:
                    stats['nb_images'] += 1
                    stats['taille_images'] += taille
                elif extension in extensions_videos:
                    stats['nb_videos'] += 1
                    stats['taille_videos'] += taille
                elif extension in extensions_audio:
                    stats['nb_audio'] += 1
                    stats['taille_audio'] += taille
    
    # Convertir les tailles en Mo et Go
    resultat = f"""
    Statistiques des fichiers :

    Fichiers TXT : {stats['nb_txt']} fichiers - {round(stats['taille_txt'] / (1024*1024), 2)} Mo
    Fichiers PDF : {stats['nb_pdf']} fichiers - {round(stats['taille_pdf'] / (1024*1024), 2)} Mo
    Images : {stats['nb_images']} fichiers - {round(stats['taille_images'] / (1024*1024), 2)} Mo
    Vidéos : {stats['nb_videos']} fichiers - {round(stats['taille_videos'] / (1024*1024), 2)} Mo
    Audio : {stats['nb_audio']} fichiers - {round(stats['taille_audio'] / (1024*1024), 2)} Mo
    TOTAL : {stats['nb_total']} fichiers - {round(stats['taille_totale'] / (1024*1024*1024), 2)} Go
    """
    
    return resultat


html_str = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="refresh" content="5">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Tinos:ital,wght@0,400;0,700;1,400;1,700&display=swap');
    </style>
</head>

<body>
    <header>
        <button>Accueil</button>
        <h1>Projet Triple A</h1>
        <button>Rechercher</button>
    </header>
    <main>
        <div class="systeme">
            <h2>Informations Système</h2>
            <span>Nom: {nom_machine()}</span>
            <span>OS: {systeme_exploitation()}</span>
            <span>Nombre d'utilisateur: {nombre_utilisateurs_connectes()}</span>
        </div>

        <div class="cpu">
            <h2>Informations CPU</h2>
            <span>Nombre de coeurs: {nb_coeur()}</span>
            <span>Fréquence: {frequence_cpu()}</span>
            <span>Pourcentange d'utilisation: {pourcentage_utilisation_cpu()} %</span>
        </div>

        <div class="memoire">
            <h2>Informations Mémoire</h2>
            <span>RAM utiliser:{ram_utilisee()}</span>
            <span>RAM total:{ram_totale()}</span>
            <span>Pourcentage:{pourcentage_utilisation_ram()} %</span>
        </div>

        <div class="reseau">
            <h2>Informations Réseaux</h2>
            <span>Adresse IP: {adresse_ip_principale()}</span>
        </div>

        <div class="procesus">
            <h2>Informations procesus</h2>
            <span>Classement des plus gourmants: </span>
            <span>{top_3_processus_gourmands()}</span>
        </div>

        <div class="fichier">
            <h2>Informations fichier</h2>
            <span>{stats_fichiers()}</span>
        </div>
    </main>
    <footer>
        <span>© 2025 Monitoring VM - Tous droits réservés</span>
    </footer>
</body>
</html>
"""


with open('projet.html', 'w', encoding='UTF-8') as fichier:
    fichier.write(html_str)
