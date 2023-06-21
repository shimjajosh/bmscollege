
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.mail import message
from .models import *
from django.shortcuts import render, redirect
# Create your views here.
def home(request):
    return render(request,"home.html")
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render (request,"application.html")
        else:
            message.info(request,"invalid credentials")
            return redirect('login')
    return render (request,"login.html")

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already exists. please try other username")
                return redirect('register')
            elif User.objects.filter(password=password).exists():
                messages.info(request, "password already exists. please try other password")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('login')
                print("user created")
        else:
            messages.info(request, "password not matching")
            return render('register.html')
        return redirect('/')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
def newpage1(request):
    return render(request,"newpage1.html")

def newpage2(request):
    return render(request,"newpage2.html")
def application(request):
    departments = Department.objects.all()
    d = {'departments': departments}
    return render(request,"application.html",d)

def load_courses(request):
    department_id = request.GET.get('department')
    courses = Courses.objects.filter(department_id=department_id).order_by('name')
    return render(request, 'courses_dropdown_list_options.html', {'courses': courses})
