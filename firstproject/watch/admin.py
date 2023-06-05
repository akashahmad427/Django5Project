from django.contrib import admin
from .models import Sellinfo,Photo
# Register your models here.
@admin.register(Sellinfo)
class SellAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'father_name', 'cnic', 'address','city', 'email', 'phone')

@admin.register(Photo)
class image(admin.ModelAdmin):
    list_display = ('id','img')