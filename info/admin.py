from django.contrib import admin
from .models import ParkData, ParkDataHistory
from .models import ManholeData, ManholeDataHistory
from .models import BillBoardData
# Register your models here.
admin.site.register(ParkData)
admin.site.register(ParkDataHistory)
admin.site.register(ManholeData)
admin.site.register(ManholeDataHistory)
admin.site.register(BillBoardData)
