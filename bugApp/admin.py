from django.contrib import admin
from bugApp.models import Ticket, SomeUser 
from django.contrib.auth.admin import UserAdmin

admin.site.register(SomeUser, UserAdmin)
admin.site.register(Ticket)