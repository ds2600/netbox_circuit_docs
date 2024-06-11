from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import CircuitDocument
from .forms import CircuitDocumentForm
from dcim.models import Circuit

def upload_document(request, circuit_id):
    circuit = get_object_or_404(Circuit, pk=circuit_id)
    if request.method == 'POST':
        form = CircuitDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.circuit = circuit
            document.save()
            return HttpResponseRedirect(circuit.get_absolute_url())
    else:
        form = CircuitDocumentForm()
    return render(request, 'netbox_circuit_docs/upload_document.html', {'form': form, 'circuit': circuit})

