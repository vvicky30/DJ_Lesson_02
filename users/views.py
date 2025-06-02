from django.shortcuts import render

# Create your views here. : here we are going to create views of users django app  here we are going to view register_view page 
def register_view(request):
    return render(request, "users/register.html")   # for viewing page here we added path to register.html file which weill be dedicated to users django app [as tamplate folder within users and users folder in the template folder containing register.html file ]
