from django.contrib import admin
from chat.models import Room


# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
     list_display = ['pk','name','slug']