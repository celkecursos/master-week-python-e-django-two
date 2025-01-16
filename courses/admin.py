from django.contrib import admin

from .models import Home
from .models import ContactMessage
from .models import Contact

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'address')
