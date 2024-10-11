from django.contrib import admin

# Register your models here.
from .models import Category,Admin,AddVehicle


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_id', 'parking_area_no', 'vehicle_type', 'vehicle_limit', 'parking_charge', 'status', 'doc')

admin.site.register(Category,CategoryAdmin)

class AdminAdmin(admin.ModelAdmin):
    list_display=('id','name','username','password')
admin.site.register(Admin,AdminAdmin)


class AddvehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'vehicle_no', 'parking_area_no', 'vehicle_type', 'parking_charge', 'status', 'arrival_time')
admin.site.register(AddVehicle,AddvehicleAdmin)