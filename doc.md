#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

@author exe90


"""
pip install django
django-admin startproject social
python manage.py runserver
pip freeze >requirements.txt
echo "Social network" >> README.md
git init
touch .gitignore
git add .gitignore

git status
git reset
git status
git add .

git commit -m 'initial commit'
git remote add origin https://github.com/exe90/Social.git
git push -u origin master

pip install -r requirements.txt
python manage.py startapp base

#Settings
'base.apps.BaseConfig'
'DIRS': [os.path.join(BASE_DIR, 'templates')],