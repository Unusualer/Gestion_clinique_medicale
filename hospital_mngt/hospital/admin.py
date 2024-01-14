from django.contrib import admin
from.models import Doctor, Patient, Nurse, Appointment

admin.site.site_header = 'Hospital Management'

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['Name', 'SP']
    list_filter = ['SP']
    #list_display_links = ['SP']


# Register your models here.
admin.site.register(Doctor,DoctorAdmin)
#admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Nurse)
admin.site.register(Appointment)