1). create project folder
2). pyenv local python-version
3). mkvirtualenv project-name // better use project-name as env name
4). workon project-name // switch to project env
5). pip freeze //check any package installed
6). pip list // show all the package with version info
7). pip show django // show django version
8). pip install django==version // install django inside the virtualenv folder
9). django-admin startproject name // create a main project folder
10). after manage.py show up then switch to python manage for the main control command
11). in vscode, command+p, select interpreter, pick the virtual name
12). install pep8 for VS code
13). git init // for git
14). create .gitignore
15). goto gitignore.io, pick the framework for ignore
16). git init // setup .git folder
17). git add . && git commit -m "Initial commit"

---

18). python manage.py runserver
19). once the server is running, db.sqlite3 created
20). within btre folder, setting is the important one
21). within setting, allowed hosts [] is for server deployment
22). root_urlconf is the url config file for the route
23). templates , the html templates
24). wsgi - django build service
25). databases - db parameter, engine
26). auth - server passwords
27). static url - all the assets files

---

28). urls.py - routing file
29). path(route/ views) as a complete API

---

30). wsgi - web application communicate with app services

---

31). create app
32). python manage.py startapp pages
33). pages folder is at the same level with main project folder
34). migrations - in case there is dbase that migrated, for this app, we won't have any database
35). admin for admin login, we are not applying admin for this app
36). apps.py - pagesconfig link with setting file
37). models.py - database
38). tests.py - for testing
39). views.py - link url to "methods"

---

40). register app inside the btre/settings.py -> installed_apps 4. btre.pdf
41). create urls.py inside pages folder
42). add the urls path
43). views.py add the callback function
44). brte.urls add the / and route to pages.urls

---

45). in the project.setttings.py, add the templates inside the DIRS[]
46). add tempates for the project by templates/pages
47). add index and about html files
48). pages.urls.py add path
49). pages.views.py add functions for the route html pages

---

50). create partial for the template pages
51), under templates folder add the base.html for the main partials
52). add the extends into index, about.html

---

53). import frontend files into static folder
54). create static folder under btre folder
55). define the static condtions under btre.settting static then  
55). build all the folders under project -> static by
python manage.py collectstatic
\*\*\* there are 2 static folder in different location
56). the project static should skip not to deploy
57). add the /static inside gitignore
