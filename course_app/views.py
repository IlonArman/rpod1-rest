from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Menu  # Добавьте импорт вашей модели Menu

def home_page(req):
    return render(req, "./menu/home_page.html")

def aboutus_page(req):
    return render(req, "./menu/aboutus.html")

def menu_page(req):
    menues = Menu.objects.all()  # Извлекаем все объекты Menu из базы данных
    return render(req, "./menu/menu.html", {'menues': menues})  # Передаем объекты в шаблон

def more_dishes_page(req):
    return render(req, "./menu/more_dishes_page.html")

def dishes_page(req):
    return render(req, "./menu/dishes.html")

def login_page(req):
    if req.method == 'POST':
        form = AuthenticationForm(req, data=req.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(req, user)
                return redirect('home_page')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(req, "./user/Login.html", context)

def signup_page(req):
    if req.method == "POST":
        form = NewUserForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
    else:
        form = NewUserForm()
    context = {
        'form': form
    }
    return render(req, "./user/Sign.html", context)

def more_dishes(req):
    return render(req, "./menu/more_dishes.html")

def logout_req(req):
    logout(req)
    return redirect('home_page')
