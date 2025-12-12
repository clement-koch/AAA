Projet Triple A —

Ce projet affiche en temps réel plusieurs informations importantes du système : CPU, mémoire, machine, utilisateurs, et processus.

🖥️ Fonctionnalités

Monitoring CPU :
Nombre de cœurs

Fréquence actuelle

Pourcentage d’utilisation

Monitoring Mémoire :
RAM totale

RAM utilisée

Pourcentage utilisé

Informations Système
Nom et OS de la machine

Heure de démarrage

Durée de fonctionnement (uptime)

Nombre d’utilisateurs connectés

Adresse IP principale

Processus
Liste des 20 premiers processus classés par utilisation CPU

Liste des 20 premiers processus classés par utilisation RAM

Top 3 des processus les plus gourmands

📂 Organisation du projet :

script.py → script Python qui récupère toutes les informations système

style.css → style de la page

projet.html → page finale générée automatiquement dans le script

README.md → documentation du projet

🔧 Technologies utilisées Technologie Rôle Python Récupération des données système psutil Lecture CPU, RAM, processus Platform / datetime Infos machine + date/heure HTML / CSS Affichage de la page Git / GitHub Versionning + collaboration

Objectif du projet

Créer un tableau de bord simple permettant de visualiser l’état du système à un instant T.
