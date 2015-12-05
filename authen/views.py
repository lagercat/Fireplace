from django.shortcuts import render
from django.contrib.auth.models import User
from forms import UserForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.template import loader
from models import Account, Badge

def app_login(request):
    if request.method == 'GET':
        return render(request, "authen/login.html")
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/submit')
            else:
                print "Disabled account"
        else:
            print "Invalid data"
    return render(request, 'authen/login.html')

def index2(request):
    template = loader.get_template('authen/index.html')
    return  HttpResponse(template.render())

def index(request):
    template = loader.get_template('authen/index.html')
    return  HttpResponse(template.render())

def register(request):
     if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            acc = Account(new_user)
            acc.save()
            login(new_user)
            return HttpResponseRedirect('/index')
     else:
        form = UserForm()

     return render(request, 'authen/register.html', {'form': form})

