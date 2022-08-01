https://www.youtube.com/watch?v=b4iFyrLQQh4i

1). Project assets setup
a). theme selection
https://demo.w3layouts.com/demos_new/template_demo/07-03-2020/estate_liberty-demo_Free/58112989/web/index.html
b). or another template resources
https://preview.colorlib.com/#konato
c). lightbox css
https://lokeshdhakar.com/projects/lightbox2/

2). create project folder
3). pyenv local python-version
4). mkvirtualenv project-name // better use project-name as env name
5). workon project-name // switch to project env
6). pip freeze //check any package installed
7). pip list // show all the package with version info
8). pip show django // show django version
9). pip install django==version // install django inside the virtualenv folder

---

## Build the main project folder

10). django-admin startproject name // create a main project folder then control job will pass the manage.py
11). after manage.py show up then switch to python manage for the main control command
12). in vscode, command+p, select interpreter, pick the virtual name
13). install autopep8 for VS code pip install autopep8

---

Git setup

---

14). git init // setup git by creating .gitignore
15). goto gitignore.io, pick the framework for ignore
16). git init // setup .git folder
17). git add . && git commit -m "Initial commit"

---

Main project files after creating the django folder

---

18). python manage.py runserver
a). go to localhost:8000, if the page is up then the inital setup is correct
19). once the server is running, db.sqlite3 created. this is not the db for real application
20). within btre folder, settings.py is the important one
a). within settings, allowed hosts [] is for server deployment, server provide IP address
b). root_urlconf is the url config file for the route that points to the project.urls
c). templates , the html templates to clients, all the pages are group together
d). wsgi - django build service
e). databases - db engine with login username, password.
f). auth - server passwords
g). static url - all the assets files

20). urls.py - routing file
21). path(route/ views) the path links to a views or another file for sub-route views as a complete API

22). wsgi - web service gateway interface. how web service communicate with app application and how app application chains process for request

---

create first app - pages app pull models and html pages together

---

23). python manage.py startapp pages
24). pages folder is at the same level with main project folder
25). Within the folder
a). migrations - in case there is dbase that migrated, for this app, we won't have any database
b). admin - any info need to show in the admin area. for admin login, we are not applying admin for this app
c). apps.py - PagesConfig function link the app with register under project settings.py file
d). models.py - database structure with all the fields
e). tests.py - for testing
f). views.py - link url to "methods" as "control"

---

## step 1 : Register the app inside the main project folder

26). register app inside the btre/settings.py -> installed_apps 4. btre.pdf
27). in case, VScode with formatted autoPEP8 not install error message then pip install autopep8

---

## step 2 : update the urls

28). create urls.py inside pages folder, (App won't create the urls.py automatically, so we create the urls.py)
29). add the urls path within the urlpattens[] (7b pages.urls.py)
a). views.index as the callback function to the views.py function and give a name as "index" for easy access the path
30). views.py add the callback functions (7c. pages.views.py)
31). go back to the project brte.urls.py add the / and include the route to pages.urls. Set the route searching order by arrange the API from top to the bottom. Usually, admin/ should be the last one (7d. btre.urls.py)

---

## step 3 : update the templates for render the html

32). in the project.setttings.py, add the templates inside the DIRS[]
(7d. btre.settings.py)
33). add tempates for the project by creating templates/pages for "/index.html" and "/about.html"
a). add index and about html files into the folder
b). for testing purpose, add simply h1 tage for both files
34). pages.urls.py add about path (8. pages.urls.py)
35). pages.views.py add functions for the about route html (7b. pages.views.py)

---

## Step 4: create partials by setup base.html for header section

36), under templates folder add the base.html for the main partials
37). add the extends as the first line of {% base.html %} into index, about.html

---

## Step 5. setup assets files from template

38). import frontend files into static folder
39). create static folder under btre folder
copy (btre_resources ->btre theme ->dist ->assets -> css, js, webfonts) to main project static (btre -> static)
40). create img folder, not all the img need to copy.
41). image related to home, realitor will upload to admin
42). only copy lightbox, and logo.prn into btre->static->img
43). a). define the static conditions under btre.settting static then
(9. btre.settings.py) (add 2 lines of static setting under static section)
b). first line is link the root directory with static
c). last line is set the source of the static files
44). copy all the static files from main project to project -> static by

python manage.py collectstatic

\*\*\* there are 2 static folder in different location, the only with admin is the final static folder and going to deploy
60). the project static should skip not to deploy
61). add the /static inside gitignore to skip the file

---

## Step 6 : building base html partials one by one

62). copy the resouces->index.html file to base.html, cut out all the mid-section (10. base.html)
a). keep the header and JS script part as a base.html
b). update the assets part by {% include static %} as the top
c). update the assets/ path by {% static 'css/all.css' %} and so on 10.base.html.pdf

63). keep the top bar and Nav bar and footer inside the base.html
64). after testing the base.html then refactor the base.html into partials
a). base.html should contains header, <body> just with one line {% block content %} {% end block %} and <script>

---

## Step 7. create partials folder under template folder

65). move all the section into different html files
a). create \_topbar.html, \_navbar.html, \_footer.html
b). move each sections into the files
c). from the base.html, {% include 'partials/_topbar.html' %} and so on
66). each of the partils use {% load "static" %} at the top
a). make sure fixed the logo to "static" wthin the nav bar
b). check the rest of the partials for any possible fixes

---

## Step 8 : build the index and about html 12. pdf

67). build the index.html by copying the showcase section before the footer section.
68). same for about, copy all the section from about.html into template.about.html, make sure checking for any image files and update the imag path
69). within the pages/index and about.html, replace any links with {% url "index" %} or "about"
a). (index and about) are where we defined withn the pages/urls.py
name='index'
b). we don't setup the listings.html yet so we leave it alone and come back to update the href="listings.html"
70). want to fix the link highlight by spot the <li> with "active"
and write the conditional statement
{% if "/" == request.path %} for both files

---

## Step 9: build listings app for the housing content and register within the project settings.py

70). create listing app
python manage.py startapp listings //for all the listing searching page
python manage.py startapp realtors // realtors admin models
71). within the templates add listings folder -> create listing.html, listings.html, search.html
72). within listings folder add urls.py, copy the same content from pages.urls.py, for the time being
73). a). register the both APPs, within the proj.setting.py installed_app, copy the settings as pagesconfig
b). put the listing route inside proj->urls.py urlpatterns, this time under the '',(second API route)

## Step 10: basic setup of APP urls and views

74). listings -> views.py add callback function based on urls.py the route, listings -> views is the main routing of the all the housing html
75). a). route API use listings/ , internal functions use listings as main collections of functions
b). listings->urls.py put /id API as <int:>
76). for template->listings->listings, listing, search, put in {% entends 'base.html' %} {% block content %}and then dummy H1 tag for the time being,
77). go test the link of the page, make sure routes are working with topbar/navbaer/footer for the time being

---

## Step 10 b: copy resources template into listings template

78). from resources folder theme pickup listings.html and copy the content into listings ->listings.html everything between Navbar/footer
79). within listings, fixed all the page links to listing, search so on
80). next will remove all the listings part of the content after link with database and render the content plus "pricing"
81). fixing the nav_bar for the features listing

---

## Step 11 : database part of the project

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
157). work on templates->base.html put a title block inside the title
158). index.html , add title block
159). about.html , add title block
160). listings.html, add title block
add the tile block for every html file

---

last app for the project - add contact
python manage.py startapp contacts
161). OPEN MODELS.PY add the data structure
162). register thee app within setting.py
163). python manage.py makemigrations contacts //create the 0001 file
164). python manage.py migrate // that will add the table inside the postgresql
165). register in contacts.admin for listing in admin panel
166). create contact.urls.py file, add the urls for form submit purpose
167). update btre->urls.py of the contact urls
168). setup contacts->views for function
169). work on templates->listings->listing.py inquiry modal section

---

form submit
170). add functions into contact.views.py
171). listing.html @180 add the method="post"
171). listing.html at 197, remove disable

---

email setup
171). update btre.settings.py // add the email setting at the bottom 53.pdf
172). contact->views.py add email function after save()
173). 54. contact.view.py

---

dashboard dynamic
174). accounts.views.py
175). template.accounts.dashboard
