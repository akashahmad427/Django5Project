from django.contrib import admin
from .models import Sellinfo
# Register your models here.
@admin.register(Sellinfo)
class SellAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'father_name', 'cnic', 'address', 'email', 'phone')