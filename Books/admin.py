from django.contrib import admin
from .models import Book_Category, Books_Model

admin.site.register(Books_Model)
# admin.site.register(Students_Model)
admin.site.register(Book_Category)