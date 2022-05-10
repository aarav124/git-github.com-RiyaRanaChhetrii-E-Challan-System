from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Challan)
admin.site.register(Signup)