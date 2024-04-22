from django.contrib import admin

from .models import Newsletter, Contact, Voluteer

admin.site.register((Newsletter,Contact,Voluteer))