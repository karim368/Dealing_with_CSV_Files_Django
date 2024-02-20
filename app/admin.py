from django.contrib import admin

# Register your models here.

from app.models import *

class Custom1(admin.ModelAdmin):
    list_display = ['bank_name']

class Custom2(admin.ModelAdmin):
    list_display = ['ifsc','branch']

admin.site.register(Bank)
admin.site.register(Branch)