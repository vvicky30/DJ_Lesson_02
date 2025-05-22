# here we made new urls.py which is dedicated to posts app here only which has now routes in the 'urlpatterns' list to the views of posts app 
from django.urls import path
from . import views   # importing views for giving path to web pages using urlpatterns(routes)

urlpatterns = [
    path('', views.posts_list ),    # here we added the path/route to posts_list views which is in the views.py(dedicated to posts app only) 
]
