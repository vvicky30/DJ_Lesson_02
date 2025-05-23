from django.shortcuts import render
from .models import Post # importing Post data model class from models.py file 
#from django.http import HttpResponse  # this will used to echoes-in the corresponding slug of the post to the respective post-page  [for testing] 
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