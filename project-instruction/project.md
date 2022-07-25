https://demo.w3layouts.com/demos_new/template_demo/07-03-2020/estate_liberty-demo_Free/58112989/web/index.html
https://preview.colorlib.com/#konato

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

setup assets files from template
53). import frontend files into static folder
54). create static folder under btre folder
copy (btre_resources ->btre theme ->dist ->assets -> css, js, webfonts) to main project static (btre -> static)
55). img folder, not all the img need to copy.
56). image->home, realitor will upload to admin
57). only copy lightbox, and logo.prn into btre->static->img
58). define the static condtions under btre.settting static then  
59). copy all the static files from main project to project -> static by

python manage.py collectstatic

\*\*\* there are 2 static folder in different location, the only with admin is the final static folder and going to deploy
60). the project static should skip not to deploy
61). add the /static inside gitignore to skip the file

---

62). open dist->assets->index.html copy 3 css link into meta area
go to bottom copy JS script link to the bottom of <body> base.html
63). update the assets/ path by {% static 'css/all.css' %} and so on 10.base.html.pdf

---

64). add the top bar and Nav bar and footer inside the base.html
65). after testing then refactor the base.html into partials
create partials under template folder
66). move all the section into different html files
67). fixed the log wthin the nav bar
68). copy the rest of the content into index.html
69). same for about, copy all the section freom about into template.about.html, make sure checking for any image files and update the imag path

---

70). create listing app
python manage.py startapp listings //for all the listing searching page
python manage.py startapp realtors // admin models
71). withing the templates add listings folder -> listing.html, listings.html, search.html
72). listings folder add urls.py, copy the same content from pages.urls.py
73). a). put the APP inside the proj.setting.py installed_app
b).put the listing route inside proj->urls.py urlpatterns

---

74). listings -> views.py add callback function for the route
listings -> views is the main routing of the all the html
75). route API use listings/ , internal functions use listings as main collections of functions

---

76). from resources folder theme pickup listings.html and copy the content into listings ->listings.html everything between Navbar/footer
77). fixed all the page links to listing, search so on
78). next will remove all the listings part of the content after link with database and render the content plus "pricing"
79). fixing the nav_bar for the features listing

---

here is the database part of the project
80). install postgres
https://postgresapp.com/
https://www.pgadmin.org/
open postgre
initialize // should get 3 db
open postgres
postgres will open terminal shell
\password postgres // create user password
CREATE DATABASE btredb OWNER postgres; // create database
\l // inspect the database
\q // exit the shell, we are going to work on the database from django and through pgadmin 4
open pgadmin //may take awhile to starup
input password
right click server // to create server
register server, pick the server name,
under connection, host : input localhost and then input the password for the postgres login
dbserver->databases->pick btredb
https://lifewithdata.com/2021/12/08/sql-tutorial-how-to-install-postgresql-and-pgadmin-on-mac/

https://www.geeksforgeeks.org/postgresql-rename-database/
under btredb , right click, properties->security, privileges add new rules
grantee pick postgres, privileges -> all , grantor -> postgres
save
https://dev.to/tieje/how-to-install-psycopg2-on-an-m1-mac-mie
export PG_HOME=/Libray/PostgreSQL/14
export PATH=$PATH:$PG_HOME/bin

81). pip install psycopg2
pip install psycopg2-binary
https://www.youtube.com/watch?v=SM8YqCy2W8o

psycopg2 is hard to install
https://pysql.tecladocode.com/section05/lectures/04_psycopg2_vs_psycopg2-binary/

install psycopg2-binary is fine
82). update setting for database engine
83). stop the server then
python manage.py migrate // mirgrate database into postgresql (make sure postgre server is still on)
if no error message then installation of database is working
goto pgadmin to check the database
84). after migration, restart server, no more migration error
85). define schema for each database
86). go to each APP (listings folder) -> model.py
87). update the model.py under listings, realtor folder
88). migrate the models into postgre by
a). pip install pillow
b). python manage.py makemigrations
89). should get 0001 files within margrations folder, those files are the "actions" to link with postgre
python manage.py sqlmigrate listings 0001
90). listings should include realtor as dependency
91). python manage.py migrate // add the models into postgre schema
92). pgadmin should see the new tables added
93). right click the tables name ,view // inspect data within the table

---

94). create admin
95). localhost:8000/admin/login // admin login page
96). python manage.py createsuperuser // under different term, make sure turn on the virtualenv
97). select users -> select admin (staff is check means admin right)
click admin can modify more settings
98). listings->admin.py to register the model within the admin
The listings "title" is from the def function
99). click listings, can add listings and all the input fields are based on model schema
100). bold fields title are required fields, others are optional input
101). so do the samething for realtor

---

102). add media into the admin
103). update the media route under btre.settings
104). update btre.urls
105). login admin add realtors
106). add listings
107). after addding, there is a media folder contains all the images according to the setting media, it will keep the date because of the setting

---

change the admin outlook
108). btre->templates create admin->base_site.html
109). btre->static->css add admin.css
110). admin area keep track all the actions before, realtor object(1) created by mistakes

---

111). change the admin area to show more data filter
a). listings : brte->listings->admin.py
b). realtor : btre->realtors->admin.py

---

post the page listings data from database
for vs code only, install pylint-django for the syntax
pip install pylint-django
112). open listings-> views.py
113). btre->templates->listings->listings.html
remove multiply listing by dynamic looping from database
114). create loop block in views.py
115). remove all 6 listings
116). replace hard code values with database values
117). btre.setting within App add humanize
118). at the more info, that will route to id

---

django paginator in a view
119). main part is template->listings->listing.html

---

fixing the index page listings
120). page->views.py, template-> pages->index.html
fixing the realtor related pages,
page-> views.py, template->pages->about.html , update the team section, card section for mvp

---

work on more info
template.listings.listing.html
copy from resources->btre_theme->dist->listing.html
from show case before footer
121). set the if block for optional images
122). modift listings->views function for listing/id

---

123). modify the search section of the main page
a). put all the selections into dictionary
b). create listings-> choices.py
c). update pages-> views.py import the dictionary
d). update templates->pages->index.html // use a for loop to get all the key. values pairs
124). within listings.url, we have the serach function, we can make use of the search
125). copy the search.html from resources-> btre_theme->dist->assets folder. Pick the code between nav_bar and footer. Paste into template->listings->search.html
126). the search page is very similar to listings page, we can copy the all the choices functions
copy the for loops from templates->pages->index.html

---

set filter for selection in the query
127). continue working on listings->views.py
128). within the search function add queryset to generate a listings and passing into search page
129). most of the layout of search.html is similar to listings.html, we can copy the looping structure, replace all the listing1 to 6 by the for loop

---

add search function
130). add search function within templates->pages->search.html
listings->views.py
template->pages->index.html

---

keep the search words within the field
131). keep the request.object and passing into template engine
update listings->views.py
insert "if" inside the tab templates->pages->index.html

---

user login part
django initial setup created user account for admin as basic under tables->auth_user
we still to create frontend for the user accounts
132). create account app
python manage.py startapp accounts
133). create templates->accounts->login.html, dashboard.html, register.html
134). within the accounts, create urls.py (it is not generate by startapp)
135). resigter the app within the btre->settings.py 42.pdf
136). define the route under btre.urls for main entry endpoint
137). copy listings.urls.py into accounts->urls.py , define the functions of the accounts routes
138). before the login links within the nav_bar, we need to modify the partials/\_nav_bar.html replace the login of the nav_bar at the bottom section
139). after updated the nav_bar then testing the linking route
140). update the highlight condition for the nav_bar login link same as listings part

---

141). copy the resources->bre_theme->dist->assets html into login.html, register.html, dashboard.html
142). update the header and modify the method="post"

---

django message app
143). include the django.contrib.message into btre.settings.py
144). add \_alert.html into partial folder
145). insert auth token within the register.html
146). update message module within the accounts->view.py
147). include alert partial into register.html for pop up messages
148). same message pastew into login.html
149). add fade out message feature by adding fadout within btere->static->js->main.js
150). need to include the static into django
python manage.py collectstatic
django will copy btre.static.js.main.js into static.js // copy to _the static folder with admin folder_
151). to test the effect, make sure you clear the browser cashe

---

152). coding on login under accounts->views.py
153). update the dashboard with the route
154). update the Nav_bar for logout and hide the login
155). once login, should only show the dashboard

---

156). update page title tab with dynamic
