from django.shortcuts import render,redirect
from .forms import RegisterForm, LoginForm
from .models import registerModel
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            password = request.POST.get('password')
            print(name,email,phone,password,"++++++++++++++++++++++++++++++")
            rm = registerModel(name=name, email=email, phone=phone, password=password)
            rm.save()
            return render(request,'home.html')
    else:
        form = RegisterForm()
    return render(request,"register.html", {'form': form})



def userLogin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get("username")
            pass_word = form.cleaned_data.get("password")
            
            if User.objects.filter(username=user_name).exists():
                messages.error(request, "Username already exists")
                return redirect("/")
            
            user = User.objects.create_user(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return redirect("/home/")
            else:
                messages.error(request, "User creation failed")
                return redirect("/login/")
        else:
            messages.error(request, "Invalid form data")
            return redirect("/login/")
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def home(request):
    if request.user.is_authenticated:
        return render(request,"home.html")