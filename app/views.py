"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.db import models
from .models import Blog
from .forms import CTFForm


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Домашняя страница',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Страница контактов',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'О сайте',
            'year':datetime.now().year,
        }
    )

def anketa(request):
    assert isinstance(request, HttpRequest)
    data = None
    gender = {"1" : "Мужской", "2" : "Женщина"}
    about_ctf = {"1" : "Нет, не знал", "2" : "Знаю о их существований", 
                "3" : "Знаю о их существований, участовал в них", 
                "4" : "Постоянно играю в CTF"}
    surctf = {"1" : "Нет, не хочу участвовать",
            "2" : "Да, хочу участвовать", 
            "3" : "Не уверен"}
    if request.method == "POST":
        form = CTFForm(request.POST)
        if form.is_valid():
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['city'] = form.cleaned_data['city']
            data['gender'] = gender[ form.cleaned_data['gender'] ] 
            data['about_ctf'] = about_ctf[ form.cleaned_data['about_ctf'] ]
            data['surctf'] = surctf [ form.cleaned_data['surctf'] ]
            data[ 'message'] = form.cleaned_data['message']
            form = None
    else:
        form = CTFForm()
    return render(
        request,
        'app/anketaform.html',
        {
            'form':form,
            'data':data
        }
    )

def blogpost(request, parametr):
    post_1 = Blog.objects.get(id=parametr)

    assert isinstance(request ,HttpRequest)
    return render(
        request,
        'app/blogpost.html',
        {
            'post_1' : post_1,
            'year': datetime.now().year
        }
    )

def blog(request):
    posts = Blog.objects.all()

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blog.html',
        {
            'title': 'Блог',
            'posts': posts,
            'year' : datetime.now().year, 
        }
    )