# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Books(models.Model):

    class Meta:
        ordering = ["last_name", "doljn"]

    last_name = models.CharField(verbose_name='фамилия', max_length=100)
    first_name = models.CharField(verbose_name='имя', max_length=100)
    e_mail = models.EmailField(verbose_name='почта', max_length=100)
    telephon = models.IntegerField(verbose_name='телефон', max_length=12)
    doljn = models.CharField(verbose_name='должность', max_length=200)