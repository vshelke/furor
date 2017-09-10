from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from remember.models import Entry
from remember.forms import EntryForm, SignupForm, LoginForm
from urllib.parse import urlparse

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        form_login = LoginForm()
        form_signup = SignupForm()
        return render(request, 'remember/main.html', {'f_login': form_login, 'f_signup': form_signup})
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            link = form.cleaned_data['link']
            tag = form.cleaned_data['tag']
            desc = form.cleaned_data['desc']
            img = "http://logo.clearbit.com/" + urlparse(link).hostname + "?size=48"
            e = Entry(name=name, img=img, desc=desc, link=link, tag=tag, completed=0, user=request.user)
            e.save()
            return HttpResponseRedirect('/')
    else:
        form = EntryForm()
        data = Entry.objects.filter(user=request.user.id).order_by('-id')
        return render(request, "remember/dashboard.html", {'data' : data, 'form': form})


def completed(request, id, option):
    if request.user.is_authenticated:
        e = Entry.objects.get(pk=id, user=request.user.id)
        if option == '2':
            e.delete()
        else:
            e.completed = option
            e.save()
    return HttpResponseRedirect('/')

def tag(request, tag):
    if request.user.is_authenticated:
        e = Entry.objects.filter(tag=tag, user=request.user.id)
        form = EntryForm()
        return render(request, "remember/dashboard.html", {'data' : e, 'form': form})
    else:
        return HttpResponse("Invalid Request!")

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']
            user = User.objects.create_user(username, email=email, password=password, first_name=first_name, last_name=last_name)
            user.save()
            user_login = authenticate(request, username=username, password=password)
            if user_login is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Error Occured!")

    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    form_login = LoginForm()
    form_signup = SignupForm()
    return render(request, 'remember/main.html', {'f_login': form_login, 'f_signup': form_signup})

def u_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse('Error Occured!')
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    form_login = LoginForm()
    form_signup = SignupForm()
    return render(request, 'remember/main.html', {'f_login': form_login, 'f_signup': form_signup})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
