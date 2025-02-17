# Upload WebSocket Application

Ce projet est une application de démonstration pour un système d'upload utilisant l'IA. Il inclut un environnement conda spécifié dans `environment.yml` et un script Python `client.py` pour tester le serveur. Le serveur peut être démarré en utilisant `python manage.py runserver`.

## Installation

### Prérequis

- [Conda](https://docs.conda.io/en/latest/miniconda.html) (Miniconda ou Anaconda)
- [Git](https://git-scm.com/)

### Étapes

1. Clonez le dépôt Git :

   ```sh
   git clone https://github.com/Zaineb-bf12/upload_ws.git
   cd upload_ws
2. Créez l'environnement conda à partir du fichier environment.yml :
   ```sh
   conda env create -f environment.yml
3. Activez l'environnement :
   ```sh
   conda activate upload_ws

4. Démarrer le serveur Redis
Pour démarrer le serveur Redis avec Docker, exécutez :
   ```sh
     docker run --name redis -p 6379:6379 redis

4. Démarrer le serveur
Pour démarrer le serveur, exécutez :
   ```sh
   python manage.py migrate
   python manage.py runserver


5. Tester avec le client Python
Pour tester le serveur avec le script client, exécutez :
   ```sh
   python client.py
