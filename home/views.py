from django.shortcuts import render, redirect
from home.models import Contact, Sinup
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from blog.models import Post
import requests
from blog.models import Post
import random
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    #view = Post.views.[50
    allPosts = Post.objects.all().order_by('-views')
    context = {'allPosts': allPosts}
    return render(request, 'home/home.html', context)

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

mydict={} # creating the dicitnary for the opt.
def sinuphandle(request):
    if "sinup" in request.POST:
        OTP_CODE = random.randrange(100000, 999999)
        mydict['name'] = request.POST['name']
        mydict['username'] = request.POST['username']
        mydict['email'] = request.POST['email']
        mydict['phone'] = request.POST['phone']
        mydict['password'] = request.POST['password']

        # rechapcha  by google .
        clientkey = request.POST['g-recaptcha-response']
        secretkey = '6Lf6H20aAAAAAE1ZPPqFCRJYnJpAVn9C4paWjCNv'
        capthacaData = {
            'secret': secretkey,
            'response': clientkey
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify ', data=capthacaData)

        # checking if any email alrady present in data
        if 'email' in request.POST:
            email = request.POST.get('email')
            if User.objects.filter(email=email).first():
                messages.warning(request, "entre another email it was taken")
                return redirect('sinup')
        # checking if any username alrady present in data

        if 'username' in request.POST:
            username = request.POST.get('username')
            if User.objects.filter(username=username).first():
                messages.warning(request, "entre another username it was taken")
                return redirect('sinup')
        # checking phone number lenght

        if 'phone' in request.POST:
            phone = request.POST.get('phone')
            if len(phone) != 10:
                messages.warning(request, "entre correct phone number")
                return redirect('sinup')

        mydict['OTP_CODE'] = OTP_CODE
        name = mydict['username']
        subject = 'welcome '
        message = f'Hi {name}  Use  {OTP_CODE} To verify Your ANcoder Blogs .'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [mydict['email']]
        send_mail(subject, message, email_from, recipient_list)
        return render(request, "home/verify.html", mydict)
        # matching the opt for the email verification.
    if "sendotp" in request.POST:
        otp = request.POST.get('otp')
        print(otp)
        if str(otp) == str(mydict['OTP_CODE']):
            print('match')
            s_user = User.objects.create_user(email=mydict['email'], password=mydict['password'],
                                              username=mydict['username'])
            # saving the student data into table.
            if s_user:
                messages.success(request, "Now you have to login yourself")
                sinup = Sinup(name=mydict['name'], email=mydict['email'],
                              phone=mydict['phone'], username=mydict['username'])
                sinup.save()
                return redirect('login')
        return render(request, "home/verify.html", mydict)
    return render(request, 'home/sinup.html')



def loginhandle(request):
    if request.method == "POST":
        email = request.POST['email']
        login_password = request.POST['login_password']
        # print(loginusername, loginpassword)
        # create a authetication
        username = User.objects.get(email=email.lower()).username
        user = authenticate(username=username, password=login_password)
        # a backend authetication
        if user is not None:
            login(request, user)
            messages.success(request, 'you login successfully')
            return redirect("home")
        else:
            messages.warning(request, "please entre correct password and email")
            return redirect("login")
    return render(request, 'home/login.html')

def logouthandle(request):
    logout(request)
    messages.success(request,'you suceesfully logout')
    return redirect('login')
def tiny(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        author = request.POST['author']
        slug = request.POST['slug']
        timeStamp = request.POST['timeStamp']
        #tumbnail = request.POST['tumbnail']
        if len(author)<2:
            messages.error(request, "Please fill the form correctly")
        else:
            tiny_post = Post(title=title, content=content, author=author, slug=slug, timeStamp=timeStamp)
            tiny_post.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, 'home/tiny.html')