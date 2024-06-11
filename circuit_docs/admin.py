from django.contrib import admin
from .models import CircuitDocument

@admin.register(CircuitDocument)
class CircuitDocumentAdmin(admin.ModelAdmin):
    list_display = ('circuit', 'document', 'uploaded_at')


