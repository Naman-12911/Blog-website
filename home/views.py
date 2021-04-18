from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact, Sinup
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from blog.models import Post
import requests

# Create your views here.
def home(request):
    return render(request, 'home/home.html') 

def about(request): 
    return render(request, 'home/about.html') 

def contact(request): 
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name, email, phone, content)

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
        
    return render(request, 'home/contact.html') 


def search(request):
    query = request.GET['query']
    if len(query) > 78:
        allPosts = Post.objects.none() 
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
    
    if allPosts.count() == 0:
         messages.warning(request, "No search results found. Please refine your query")
    params = {'allPosts': allPosts, 'query':query}
    return render(request, 'home/search.html', params) 

def sinup(request):
    if request.method == "POST":
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        if not username.isalnum():
            messages.warning(request, "name should contain only alphabet")
        if len(phone) != 10:
            messages.warning(request, "entre correct phone number")
            return redirect('sinup')
        if len(password) < 5:
            messages.warning(request, "entre strong password")
            return redirect('sinup')

        # rechapcha
        clientkey = request.POST['g-recaptcha-response']
        secretkey = '6Lf6H20aAAAAAE1ZPPqFCRJYnJpAVn9C4paWjCNv'
        capthacaData = {
            'secret': secretkey,
            'response': clientkey
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify ', data=capthacaData)

        # create the user
        myuser = User.objects.create_user(username, email, password)
        myuser.phone = phone
        myuser.name = name
        sinup = Sinup(name=name, email=email, phone=phone, password=password, username=username)
        sinup.save()
        messages.success(request, "your account has been create succesfully")
        messages.success(request, "now you have to login yourself")
        return redirect('login')
    else:
        return render(request, 'home/sinup.html')


def loginhandle(request):
    if request.method == "POST":
        login_username = request.POST['login_username']
        login_password = request.POST['login_password']
        # print(loginusername, loginpassword)
        # create a authetication
        user = authenticate(username=login_username, password=login_password)
        # a backend authetication
        if user is not None:
            login(request, user)
            messages.success(request, 'you login successfully')
            return redirect("home")
        else:
            messages.warning(request, "please entre correct password and email")
            return redirect("login")
    return render(request, 'home/login.html')

def handleLogout(request): 
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home') 
