from urllib import request

from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login,get_user_model
from django.http import HttpResponse
from django.shortcuts import redirect, render


def home_page(request):
    context= {
        "title":"Hello World!",
        "content":"Welcome to the homepage."
    }
    if request.user.is_authenticated():
        context["premium_content"]="yesaa"
    return render(request,"home_page.html",context)

def about_page(request):
    context={
        "title":"About Page",
        "content":"Welcome to the about page."
    }
    return render(request,"home_page.html",context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None) 
    # istace of for clas
    context={
        "title":"Contact Page",
        "content":"Welcome to the contact page.",
        "form":contact_form
    }
    if contact_form.is_valid(): 
        print(contact_form.cleaned_data)
    # if request.method=='POST':
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request,"contact/view.html",context)



def login_page(request):
    form=LoginForm(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(request,username=username,password=password)
    

        if user is not None:
            # print(request.user.is_authenticated())
            login(request,user)
            #redirect to a success pageself.
            #context['form] = LoginForm()

            return redirect("/login")
        else:
            # return an 'invalid login' error message
            print("Error")
    return render(request,"auth/login.html",context)

User = get_user_model()
def register_page(request):
    form=RegisterForm(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username=form.cleaned_data.get("username")
        email=form.cleaned_data.get("email")
        password =form.cleaned_data.get("username")
        new_user=User.objects.create_user(username,email,password)

    return render(request,"auth/register.html",context)
