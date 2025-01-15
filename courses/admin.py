from django.contrib import admin

from .models import Home
from .models import ContactMessage

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject')
