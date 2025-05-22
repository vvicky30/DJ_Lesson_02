from django.shortcuts import render

# Create your views here.
def posts_list(request):
    return render(request, 'posts/posts_list.html')
    #as this will automatically detect posts_list.html in posts folder within templates folder(dedicated to posts app only) 
              #as we already register the 'templates' directory to list of templates (in DIR dictionary there) in settings.py 
             # over that we also registered the posts app in settings.py by adding 'posts' to installed apps list there 