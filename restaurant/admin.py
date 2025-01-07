from django.contrib import admin
from .models import menuModel, bookingModel

# Register your models here.
admin.site.register(menuModel)
admin.site.register(bookingModel)
