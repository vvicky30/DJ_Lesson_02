# here we made new urls.py which is dedicated to posts app here only which has now routes in the 'urlpatterns' list to the views of posts app 
from django.urls import path
from . import views   # importing views for giving path to web pages using urlpatterns(routes)

app_name = 'posts'  #here we designated the this url file as dedicated to 'posts' (django app) where it stores only urls to views of posts-app pages
# we're doing so because in broader and larger project we're not going to make a single django-app but going to make multiple django app.

urlpatterns = [
    path('', views.posts_list, name= "list" ),    # here we added the path/route to posts_list views which is in the views.py(dedicated to posts app only) 
                                                  #here we also added name paramter in giving path to views posts_list ,this because we want to make this url as named-url ,here it's named as "posts"
    path('new-post/', views.post_new, name= "new-post" ),# here we made this named url as 'new-post' giving routes posts_new view.[all these for sake of authrization: protecting our new-post page from unauthorized user ; user who don't loged-in not allowed to new-post page to contribute]
    path('<slug:slug>', views.post_page, name= "page" ), # here we're adding routes to the views 'post_page' with named-url giving name as "page" for right now 
     #here we are using slug as the path converter which will automatically adds corresponding slug to the end of the actual url last-page ex:localhost:8000/posts/first-post
     # tis will automatically takes corresponding slug of post and adds it to the last page url because we here used slug itself as parameter to the slug path converter.
]

'''
[This is how we protecting new-post page from unauthorized users who wnat to acess that page without loged-in]


Django processes urlpatterns top to bottom — first match wins.
So consider this:
# WRONG ORDER (will cause issues) like new-post path after slug or catching path patterns:-
urlpatterns = [
    path('<slug:slug>', views.post_page, name="page"),
    path('new-post/', views.posts_new, name="new-post"),
]
#This will create a problem if :
If a user visits: /...../posts/new-post/
Django will match this with: path('<slug:slug>', views.post_page, name="page")
treating "new-post" as the slug, and trying to find a post with slug "new-post" — even if it doesn't exist — which is not what we want.

Correct Order:
urlpatterns = [
    path('', views.posts_list, name="list"),
    path('new-post/', views.posts_new, name="new-post"),  # put this BEFORE slug
    path('<slug:slug>', views.post_page, name="page"),    # generic path match last [with slug-path converter]
]

This way:
Django checks for /new-post/ first
Only if none of the specific routes match, it tries <slug:slug>
'''