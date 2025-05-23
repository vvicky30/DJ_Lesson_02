from django.contrib import admin
from .models import Post #here i am importing my data model class from models.py  
# for creating super user we have to run this command on cli : Dj_lesson_02\myproject>py manage.py createsuperuser
# it will ask further for super username and e mail id (which's not compulsory) and new password to be set for super user 
#after creating superuser now we can go to runserver and at browserside go to admin page and gives superuser credential and log in.
# it takes us to django administration page where there's built-in feature for administrator to add user or change unsers or make group of users.
# we can also add other features for  managing content of our website ; like here in our case managing the 'posts' (adding post with title , content and slug etc   or delete the post etc)  
# so by all these means this admin page will be acting as content-management-system(CMS) page for our website.

# Register your models here : for adding features regarding our data-models class , we have to register it here in admin.py through which we can mange our categorical data corresponds to a data model class. 
admin.site.register(Post)