from django.shortcuts import render , redirect  # we need redirect function as once user registered succesfully then it will be redirected to the list_page
# for user registation purpose we're now importing usercreationforms class from django authentication froms.
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#here authentication form used for authenticate users during user-login like if they're already registered then user is authenticated to be loged-in 
from django.contrib.auth import login # this subclass will allowed user to be logedin after from validation sucessfull
from django.contrib.auth import logout # this subclass will allowed user to be logout.
# Create your views here. : here we are going to create views of users django app  here we are going to view register_view page 
def register_view(request):
    if request.method == "POST": # it means if on web-page(register) if user able to submit its info then ultimately post method will be invoked.
        form = UserCreationForm(request.POST) # if that happen then we will save the submitted info of user (through invocation of post method) to the form-object of createuserform class by calling its constructor (will be same name as class) with argument as request.POSt(which will be the submitted content)
        if form.is_valid():  # validation: this will return true or false like form contains any info of user or not?
            # if yes its has user-info ; then it will be true and info will be saved
            login(request, form.save()) # in this way after validation from succesfully we're allowing user to be logged-in as well who registered themselves by submitting registration data; using that same registation data(that we get here through 'form.save()') we allowed them to be logged-in. 
            # so after saving user-info ; we will be redirecting user to list-page 
            return redirect("posts:list")  # here "posts:list" posts is app name(which we designated in urls.py of 'posts') whereas list is list page of it.
    else:
        form = UserCreationForm() # here we create object of usercreationfrom class , through which new user is created or registered 
    return render(request, "users/register.html", {"form": form})   # for viewing page here we added path to register.html file which weill be dedicated to users django app [as tamplate folder within users and users folder in the template folder containing register.html file ]
                     # so on register.html (register page) through this object to usercreationfrom class '{"form": form}' we are going to view user registation form , just on html file we have to format it little bit (like how it will be done)

"""
Summary of Conditions with Explanations:-

1. Visiting the registration page (GET request method will be invoked automatically once user vist users/registation page ):

 A. The user opens the registration URL (/register/).

 B. The request method is GET(automatically invoked).

 c. The else block runs first: an empty UserCreationForm is created.

🔄 Result: A blank registration form is displayed on the web page for the user to fill in.


2.  Submitting valid registration info (POST request method invoked):

 A. The user fills in the form and clicks submit.

 B. The request method is POST ; means the (if request.method == "POST")-> True.

 c. UserCreationForm(request.POST) is used to bind submitted data.

 D. form.is_valid() returns True because: Username is available as username is unique not duplicate.

 E. Passwords match and meet Django's security criteria.

 F. The form data is saved to the database using form.save().

 G. User is redirected to "posts:list" page. [Finally]

✅ Result: User is successfully registered and redirected to the posts list page.


3. Submitting invalid registration info (POST request method invoked):

 A. The user submits the form, but: Username already exists, or Passwords don’t match, or Password is too weak, etc.

 B. The request method is POST; means the (if request.method == "POST")-> True.

 C. form.is_valid() returns False.

 D. The form is not saved, and no redirect happens ; no another empty from gvien through else-block. 

 E. The same form is returned to the user with error messages through default return render request of viewing form.

❌ Result: User stays on the registration page and sees validation errors.
"""
#Here we're going to create login views with same approach as we did for register_views:

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST) # unlike usercreation form this authentication form will take variable number of data as in form of key and value [here key will be 'data' and data value we're passing here whatever user submit on login-page through request.POST method} 
        if form.is_valid(): 
        #after validating from ; and if its validated sucessfully then we allowed user to logged-in with user-data(same as entered by user on login-page) ; we can get data user data like this 'form.get_user()'
            login(request, form.get_user())
            
            #in case we user press icon related to acess any page(like new-post page) but login-icon ; then it should be redirected to next?_request page for which user requested to acess page[here new-post page] by pressing new-post page icon ; once user logged-in(authorized)   
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else: #else if user tryinng acess logic-page simply by pressing login-page icon then redirect user to post:lists once he/she logged-in     
                return redirect("posts:list")
    else: 
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form" : form})

#Here we're going to create logout views with same approach as we did for login_views:
def logout_view(request):
    if request.method == "POST": # it will be simple if user press log-out button which automatically invoked post-method 
        logout(request) # after which user loded-out with this rquest imedietly 
        return redirect("posts:list") # then redirect to list page of posts django application
     
