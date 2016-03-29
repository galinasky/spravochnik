# -*- coding: utf-8 -*-
from django.conf.urls import include, url, patterns
from django.contrib import admin
from book.models import Books
from django.conf import settings
from django.conf.urls import static

urlpatterns = [
    #url(r'^books/(?P<Books_id>\d+)/$', 'book.views.books', name='books'),
    url(r'^auth/login/', 'book.views.login'),
    url(r'^auth/logout/', 'book.views.logout'),
    url(r'^books/$', 'book.views.booksall', name='booksall'),
    url(r'^serch/$', 'book.views.serch'),
    url(r'^$', 'book.views.booksall', name='booksall'),
]