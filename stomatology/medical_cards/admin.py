from django.contrib import admin

from .models import MedicalCard, Record

admin.site.register(MedicalCard)
admin.site.register(Record)
