# CMix

## Installation

### Prérequis

* Installer django avec `sudo apt install python3-django`
* Sqlite3 est normalement déjà installé

### En local

* Cloner le repo `git clone git@github.com:julcar99/CMix.git`
* Lancer le serveur en local `python3 src/manage.py runserver`

## Sur une VM

### Configurer un Virtualenv

* Installer la librairie python : `pip3 install virtualenv`
* Créer le venv à la racine dans le dossier CMix `(sudo) python3 -m venv .env`
* lancer le venv  `source .env/bin/activate`
* accéder à pip sans droits root [doc]( https://stackoverflow.com/questions/19471972/how-to-avoid-permission-denied-when-using-pip-with-virtualenv )`sudo chown -R your_username:your_username path/to/virtuaelenv/` 

### télécharger les librairies 

* installer django `pip3 install django`
* installer gunicorn `pip3 install gunicorn`

### Configurer le repo

- Clone dans var/www le repo distant en https `git clone https://github.com/julcar99/CMix.git`
- renommer le fichier static en static_comp
- changer dans  var/www/Cmix/src/cmix/settings.py
```
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = [
str(BASE_DIR)+'/static_comp/',
]
```
- mettre les static `python3 manage.py colectstatic`

### lancer gunicorn

* change ownership of file owned by the root user instead of a sudo `chmod -R 777 CMix`
```
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```