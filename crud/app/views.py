from django.shortcuts import render,redirect
from . models import *
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'registration.html')
def loginn(request):
    return render(request,'login.html')

def table(request):
    stu=Student.objects.all()
    return render(request,'table.html',{'stu':stu})
def register(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        phone=request.POST['phone']
        subject=request.POST['subject']
        password = make_password(request.POST["password"])
        if Student.objects.filter(email=email).exists():
            messages.success(request,f"email already registered")
            return redirect('/')
        else:
           Student.objects.create(fname=fname,lname=lname,password=password,email=email,phone=phone,subject=subject)
           return redirect('login')
    return render(request,'registration.html')
def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        user_password = request.POST["password"]
        if Student.objects.filter(email=email).exists():
            obj = Student.objects.get(email=email)
            password = obj.password
            if check_password(user_password, password):
                return redirect("tab")
            else:
                messages.success(request,f"invalid password")
                return redirect("login")
        else:
            messages.success(request,f"email not registered")
            return redirect('loginn')
    return render(request,'login.html')

def delete(request,pk):
    Student.objects.get(id=pk).delete()
    stu=Student.objects.all()
    return render(request,'table.html',{'stu':stu})

def update(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')

        Student.objects.filter(id=uid).update(
            fname=fname,lname=lname,email=email, subject=subject, phone=phone
        )
        return redirect('tab')
    return render(request, 'table.html')
