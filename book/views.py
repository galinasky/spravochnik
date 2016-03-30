# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import request
from django.shortcuts import render_to_response, redirect
from book.models import Books
from django.contrib import auth
from django.core.context_processors import csrf
from django.template.loader import get_template
from django.template import context


# Create your views here.
def booksall(request):
    return render_to_response('booksall.html', {'books': Books.objects.all(), 'username': auth.get_user(request).username})

def serch(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        serch_id=''
        args['books'] = Books.objects.filter(last_name=serch_id)
        args['username'] = auth.get_user(request).username
        return render_to_response('booksall.html', args)
    else:
        return render_to_response('booksall.html', args)

def serch1(request, serch_id):

    return render_to_response('booksall.html', {'books': Books.objects.filter(doljn=serch_id), 'username': auth.get_user(request).username})

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        # username и password без ' !!!
        if user:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = 'пользователь не найден'
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)

def logout(request):
    auth.logout(request)
    return redirect('/')