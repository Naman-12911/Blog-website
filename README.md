# Blog-website
                                                                                      ##A blog website
In this blog webisite a login person can write the blog and comment, repaly to the blog. I use authentication in this website.
if anybody face any problem he/she can fill the contact us page.
In this website the tiny rich text editior can help you to write the blog effictevly.

## Technology stack that I uesd in this website.
 for the front-end development 
 HTML, CSS, javaScript and Bootstrap framework.
 
 Backend development
 python, Django framework.
 
Database

Sqlite

## how to run this project in your localsystem.
first you have to activate virtualenvirnment

cd ico # to go virtualenv
cd Scripts
activate
# the virtual env is activate than you have to follow another commands

you have install all the library that need of this project, you can run this command to install all the library

pip install -r requirements.txt

#Now, you have to run migartion and migrate command for the database.

python manage.py makemigrations
python manage.py migrate

# now, toy are ready to run this project in your localsystem

# python manage.py runserver
