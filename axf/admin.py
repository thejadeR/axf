from django.contrib import admin

# Register your models here.
from axf.models import Wheel

class WheelAdmin(admin.ModelAdmin):
    list_display = ['name','trackid','img']


admin.site.register(Wheel)