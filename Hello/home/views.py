from django.shortcuts import render, redirect,get_object_or_404
from datetime import datetime
from home.forms import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        context = {
            'name':'kashif',
            'age': 20
        }
        return render(request, 'home.html', {'data':context})
        # return HttpResponse('This is Home page')
    return redirect('/login')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        if Contact.objects.filter(email=email).exists() or Contact.objects.filter(phone=phone).exists():
            # User with the provided username or email already exists
            messages.warning(request, "A user with the provided username or email already exists.")
        else:
            contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
            contact.save()
            messages.success(request, "Your message has been sent!")
    return render(request, 'contact.html')

def icename(request):
    return render(request, 'icename.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return redirect('/login')
    elif request.user.is_authenticated:
        messages.success(request, "Your have been already login!")
        return render(request, 'login.html')
    return render(request, 'login.html')


def signupUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('cpassword')
        # Create the user
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('/')
        messages.warning(request, "A user that username already exists.")
        return render(request, 'login.html')
    # If request method is not POST, render the login page
    return render(request, 'login.html')


def showUser(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = request.user
            return render(request, 'show.html', {'users': user})
        else:
            return render(request,'show.html')
        
    else:
        return render(request,'login.html')
    

def delete(request,username):
    user = User.objects.get(username=username)
    user.delete()
    return redirect('/login')


def edit(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'edit.html', {'user': user})

def update(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        
        # Set the password securely
        new_password = request.POST.get('password')
        if new_password:
            user.set_password(new_password)
        
        user.save()
        return redirect('/show')
    else:
        return render(request, 'edit.html', {'user': user})