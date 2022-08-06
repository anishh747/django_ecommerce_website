
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.shortcuts import render,redirect
from home.models import Contact
from django.contrib.auth import login as auth_login


# Create your views here.

def index(request):
    return render(request,'index.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        user = authenticate(username = username ,password = pass1)

        if user is not None:
            auth_login(request,user)
            fname = user.first_name
            messages.success(request,"Logged in Successfully")
            return render(request,'index2.html',{'fname':fname})
        else:
            messages.warning(request,"Wrong Credentials")
            return redirect('/login')


    return render(request,'login.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
    
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request,"Your account has been created successfully ! Please log in to continue")

        return redirect('/login')

    return render(request,'register.html')
    
def logoutUser(request):
    logout(request) 
    messages.success(request,"Logged Out Successfully")
    return redirect('/')

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,number=number,desc=desc,date=datetime.today())
        contact.save()
    return render(request,"contacts.html")

def contacts1(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,number=number,desc=desc,date=datetime.today())
        contact.save()
    return render(request,"contacts1.html")


def payment(request):
    return render(request, 'payment.html')

def about(request):
    return render(request, 'about.html')

def about1(request):
    return render(request, 'about1.html')

def index1(request):
    return render(request, 'index2.html')

def item1(request):
    return render(request, 'items/item1.html')

def item2(request):
    return render(request, 'items/item2.html')

def item3(request):
    return render(request, 'items/item3.html')

def item4(request):
    return render(request, 'items/item4.html')

def item5(request):
    return render(request, 'items/item5.html')

def item6(request):
    return render(request, 'items/item6.html')

def item7(request):
    return render(request, 'items/item7.html')

def item8(request):
    return render(request, 'items/item8.html')

def item9(request):
    return render(request, 'items/item9.html')