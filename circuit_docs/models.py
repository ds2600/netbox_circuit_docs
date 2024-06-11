from django.db import models
from circuits.models import Circuit

class CircuitDocument(models.Model):
    circuit = models.ForeignKey(Circuit, on_delete=models.CASCADE, related_name='documents')
    document = models.FileField(upload_to='circuit_docs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
