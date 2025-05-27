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
    banner = models.ImageField(default = 'fallback.png', blank = True)#here we give option to user for uploading image file as reference picture while publishing post by using 'imagefield' model-refenrece field type.
                            # here its allowed to be leave it blank by user while creating and publishing post as bydefault its will use 'fallback.png' as deafault reference picture for published post. 
     
    def __str__(self):  # here we make instance function so during retrival it will show object's value or actual posts instead of number of posts 
        return self.title 

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

''' 
what is ORM : ORM is stands for object relational mapping , as we know our data model which we're building here will saves that categorical data from front-end end-use to the corresponding table with same name as data-model in the db at back-end
so basically here data model class that we made 'Post' will acts as table name in the db server which stores data.
with the help of ORM its facilitates the movements of data b/w our data models(which take categorical data from front-end) and table in the db at back-end 
for ORM we have to make instance of our data model class which's here 'Posts' 
then we can acess the standard functions(model-reference filds) of class(data model) using this instance/object 
we can also make the string type return instance function which gives us actual content in the data model class instead of numbers.

here is simple illustration in interactive shell for django project 
Dj_lesson_02\myproject> py manage.py shell

7 objects imported automatically (use -v 2 for details).

Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.   
(InteractiveConsole)
>>> from posts.models import Post    # we import our data model class from posts/models.py file  
>>> p= Post()  # here make instanace/Object data model class Post
>>> p     # inspect p ;    which is of object type referring to Post data model class
<Post: Post object (None)>
>>> p.title = "My first post"  #giving now title to first post by using instance to acess data model class's model reference field 
>>> p.save()  # saving it 
>>> Post.objects.all()  # retrivng all the objects for seeing the values of post 
<QuerySet [<Post: Post object (1)>]>  # here it showing there's only one 
>>> exit()   
''' 
#in interactive shell of django project
'''
so after making instance str function in our data model class; we can now see actual posts while retreiving the objects value instead of numbers: 
>>> from posts.models import Post
>>> p= Post()
>>> p.title = "My second post"
>>> p.save()
>>> Post.objects.all()
<QuerySet [<Post: My first post>, <Post: My second post>]>  # here we can see the objects values (posts) instead of numbers
'''        
# one thing should be clear that while handling media files like images we have to install pillow (which used for image manipulation)
# cmd: pip install pillow