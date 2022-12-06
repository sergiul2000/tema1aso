# from django.contrib import admin
# from scrumboard.models import List, Card
# # Register your models here.
# admin.site.register(List)
# admin.site.register(Card)
from django.contrib import admin
from .models import Room,Message
admin.site.register(Room)
admin.site.register(Message)