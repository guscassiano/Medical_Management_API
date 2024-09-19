from django.contrib import admin
from .models import Consultation, Patient


class PatientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'profession', 'address', 'city' ,'state', 'email', 'phone', 'social_name')
    search_fields = ('full_name', 'profession', 'city' ,'state', 'social_name')

class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('consultation_data', 'patient_name')
    search_fields = ('consultation_data', 'patient_name')

admin.site.register(Patient, PatientAdmin)
admin.site.register(Consultation, ConsultationAdmin)