from django.db import models
# this models are data models used to model our data(data which 's published by user as end user on web app or data which can be retrived as per end user's request on web app)
#this models that we import above from django.db is a super class through it constructor we can make our own data models class corresponding to categories of data that we're going to save on our db 
 
#here we made data model corresponds to the posts' data with title and content box and datetime stamp of publishing and slug(which's nesscary data input which is used to pin point the post by adding inputed slug to the end of url link)
# Create your models here. [here classes (our data models) will be acts as table in our db]

class Post(models.Model):
    title = models.CharField(max_length=75)  # title of posts which is using charfield as model_reference_filed type here  
    body = models.TextField()  # this will be content or text area , here we're using textfield as model_reference_field type  
    slug = models.SlugField() # this will use to identify each post with user input slug(tag) which will be added at the end of url (this is compulsory)
    date = models.DateTimeField(auto_now_add=True) #auto_now_add=True means it will add system's datetime stamp when user added or saves post at web automatically. 



#once we create our data model we have to apply for migration for our created data model in cmd terminal before we runserver.
# for that we have to create migration first  ; cmd : Dj_lesson_02\myproject>py manage.py makemigrations ; this will create migration file corresponds to our post data model with tracking id like 001 (this tracking id used to track potential modifications in dats model)
#now we have to appply this specific migration for our data model; 
''' cmd : lesson_02\myproject>py manage.py migrate        
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, posts, sessions
Running migrations:
  Applying posts.0001_initial... OK
'''
#if anyhow we modified our data model in terms of adding model-reference field or model reference type then after each modification as such we should apply migration .
#what exactly migration is , it's the command through which we create and enable migration file corresponds to our data model , this migration file then used to migrate our data from web front-end input/retirval to the db-server at backend and saves it to the table named same as our data model.

# [NOTE]: myproject(upper directory) has its own sets of standard data models for thir template database and meta-data purposes, so for this first we have to apply migration for such standard data models of project and then we can apply it for django app i.e. posts.
          #command to do that (at myproject directory) : Dj_lesson_02\myproject>py manage.py migrate