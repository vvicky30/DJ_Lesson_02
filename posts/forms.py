from django import forms  # here we import forms which is subclass used for creating our custom forms 
from . import models   # here we import our data model that we made for posting post by taking several post information from user using model reference field and types.

#now lets create our custom form here by name CreatePost(as this specific form allow user to create new-post on new-post page)
 
class CreatePost(forms.ModelForm):
    class Meta:  # in meta class we specifically give it the Post data-model class that we made
        model = models.Post
        # now if we want we modify further the reference field through which we allowed user to put post-information of diffrent kind 
        # / if not modify further then it will continue taking all data model reference field that we used in 'Post' data model-class [that also mentioned underneath Meta class]
        fields = ['title', 'body','slug', 'banner'] # not need to mention date reference field here explicitly as it will be automaticaly fetched duirng post-submit  
          
        