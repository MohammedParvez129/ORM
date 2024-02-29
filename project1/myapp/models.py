from django.db import models
from django.contrib import admin
class Book(models.Model):
     bookid=models.IntegerField(primary_key=True);
     bookname=models.CharField(max_length=20);
     author=models.CharField(max_length=50);
     price=models.IntegerField();
     publishdate=models.DateField();
class BookAdmin(admin.ModelAdmin):
     list_display=("bookid","bookname","author","price","publishdate");
