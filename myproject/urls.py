"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views   # importing views for giving path to web pages using urlpatterns(routes)
from django.conf.urls.static import static  # for registering media folder into the url
from django.conf import settings # here we import settings.py where we confidure it for media folder

urlpatterns = [
    path('admin/', admin.site.urls), # as here we can see there's already (bulit-in) path given to admin page of our web site .  // but before going to this path on browser we have to make superuser in admin.py file.
    path('', views.homepage ),     # as this will be like our main page , our web-site start from this page only , so no need to give path explicitly in quotes  
    path('about/',views.about), # as this will be our aboutpage available on  website-path/aboutpagepath like that :that's why giving path i.e. /about in quotes here 
                                 #ex: http://localhost:8000/about/    
    path('posts/', include('posts.urls'))  # here we registering url.py folder which's dedicated to posts app only by 'include' function of django.urls
                                     # and giving the path name as "posts/""
   
]
# going to add in above urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
# adding here MEDIA_URL and giving path to the media folder same as we configured in the settings.py file 

