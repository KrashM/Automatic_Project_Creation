@echo off
d:
cd path/to/project/create.py/folder
python create.py %1
cd %1 #direct to projects folder
git init
copy NUL Read.me
git add .
git commit -m "Initial commit"
git remote add origin git@github.com:"username"/%1.git
git push -u origin master
code .