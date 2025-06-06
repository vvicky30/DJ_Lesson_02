# here we made new urls.py which is dedicated to users app here only which has now routes in the 'urlpatterns' list to the views of users app 
from django.urls import path
from . import views# importing views for giving path to web pages using urlpatterns(routes)

app_name = 'users'  # no django app name is 'users' for which it designated

urlpatterns = [
    path('register/', views.register_view, name="register"),# here we added the path/route to 'register_view' views which is in the views.py(dedicated to users app only) 
                                                   # here named-url we added by name 'register'
    path('login/', views.login_view, name="login"),# here we make the named url for login view just like we did in creating named url for register view
    path('logout/', views.logout_view, name="logout")
    
]
