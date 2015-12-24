from django.contrib import admin
from .models import ParkData, ParkDataHistory
# Register your models here.
admin.site.register(ParkData)
admin.site.register(ParkDataHistory)
