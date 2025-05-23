# here we made new urls.py which is dedicated to posts app here only which has now routes in the 'urlpatterns' list to the views of posts app 
from django.urls import path
from . import views   # importing views for giving path to web pages using urlpatterns(routes)

urlpatterns = [
    path('', views.posts_list, name= "posts" ),    # here we added the path/route to posts_list views which is in the views.py(dedicated to posts app only) 
                                                  #here we also added name paramter in giving path to views posts_list ,this because we want to make this url as named-url ,here it's named as "posts"
]
