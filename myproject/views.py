#from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    
    #return HttpResponse("Hello world from homepage.")
    return render(request, 'home.html')  #as this will automatically detect home.html 
              #as we already register the templates directory to list of templates (in DIR dictionary there) in settings.py 
def about(request):
    
    #return HttpResponse("hello from aboutpage")
     return render(request, 'about.html') #as this will automatically detect about.html 
              #as we already register the 'templates' directory to list of templates (in DIR dictionary there) in settings.py 
    