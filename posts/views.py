from django.shortcuts import render
from .models import Post # importing Post data model class from models.py file 
#from django.http import HttpResponse  # this will used to echoes-in the corresponding slug of the post to the respective post-page  [for testing] 
from django.contrib.auth.decorators import login_required # here we import login_required decorator from django.contrib.auth [for preventing our post_new page to be view to unauthorized user]
# Create your views here.
def posts_list(request):
    #saving all posts-contents(Objects values) to posts-variable here
    posts= Post.objects.all().order_by('-date')  # here we're order by minus date(descending way) ; means newer posts will show rist and older post will show later succesively.
    return render(request, 'posts/posts_list.html', {'posts': posts})
    #as this will automatically detect posts_list.html in posts folder within templates folder(dedicated to posts app only) 
              #as we already register the 'templates' directory to list of templates (in DIR dictionary there) in settings.py 
             # over that we also registered the posts app in settings.py by adding 'posts' to installed apps list there 
            
            #after registering the "Post" data model class to admin.py for adding data management feature arround 'Post' data model to web-site admin-page (CMS-page)
            #now we have to showcase our actual posts with their contents on posts-page 
            # for that we have to call and save all contents of posts(objects) through acessing all objects of Post data model class  
            # and adding it as parameter to render [in dictionary type]
def post_page(request, slug):
    #return HttpResponse(slug)  # going to show echoed corresponding slug to post page [testing]
    post= Post.objects.get(slug=slug)  # instead of one post we're going to show single post based of corresponding slug(going to match slug to the slug given as argument to the function)
    return render(request, 'posts/post_page.html', {'post': post})



# as we know in python decorators used to add functionalities to exisiting function without modifying its original code within.
@login_required(login_url="/users/login/")# this logic_required decorator redirect the unauthorized-user[who's not loged-in yet] to login page [which's in the 'user' djnago app] ; 
#and in this way it protects unauthorized user to acess 'new-post' page 
# [here in case after user loged-in , it will redirect to list page of posts djnago app ; as this was done due to the redirection to post:list mentioned in login_view in 'user' app]
#[once user logged-in instead of redirecting user to post:list page we have to redirect for which user press the icon (which was here the icon of new-post page); we can do this by adding favourable logics to login_views in user-app and alligning it with login.html file]
def post_new(request):
    return render(request, 'posts/post_new.html')