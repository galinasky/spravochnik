from django.contrib import admin
from book.models import Books
# Register your models here.

class BooksAdmin(admin.ModelAdmin):
    list_display = ['last_name','first_name','doljn']
    fields=['last_name','first_name','e_mail','telephon','doljn']
    search_fields = ['last_name']
    list_filter=['doljn']


admin.site.register(Books,BooksAdmin)