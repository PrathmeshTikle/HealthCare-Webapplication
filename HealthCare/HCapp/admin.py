from django.contrib import admin

from django.contrib import admin
from .models import Contact,DoctorT,PatientT,AppointT,AppointCopy
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','contact','message']
admin.site.register(Contact,ContactAdmin)


class DoctorAdmin(admin.ModelAdmin):
    list_display=['id','user','specialty']
admin.site.register(DoctorT,DoctorAdmin)
class PatientAdmin(admin.ModelAdmin):
    list_display=['id','user','age','gender']
admin.site.register(PatientT,PatientAdmin)

class AppointAdmin(admin.ModelAdmin):
    list_display=['doctor','patient','date','time']
admin.site.register(AppointT)

class AppointCopyAdmin(admin.ModelAdmin):
    list_display=['doctor_name','patient_name','date','time']
admin.site.register(AppointCopy,AppointCopyAdmin)