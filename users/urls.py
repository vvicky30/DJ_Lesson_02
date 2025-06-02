# here we made new urls.py which is dedicated to users app here only which has now routes in the 'urlpatterns' list to the views of users app 
from django.urls import path
from . import views# importing views for giving path to web pages using urlpatterns(routes)

app_name = 'users'  # no django app name is 'users' for which it designated

urlpatterns = [
    path('register/', views.register_view, name="register")# here we added the path/route to 'register_view' views which is in the views.py(dedicated to users app only) 
]
