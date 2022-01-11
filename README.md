# RCAM-backend

### Initialisation (Windows)

1. Virtual Environment

* python -m venv {URI}
* .\venv\Scripts\activate.bat

2. Dépendances

* pip install -r requirements.txt

3. Migrations de la base de données

* python manage.py makemigrations
* python manage.py migrate

4. Lancement du serveur

* python manage.py runserver
