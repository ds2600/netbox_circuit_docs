from extras.plugins import PluginConfig, PluginTemplateExtension

class CircuitDocsConfig(PluginConfig):
    name = 'netbox.plugins.netbox_circuit_docs'
    verbose_name = 'Netbox Circuit Docs'
    description = 'Manage documents attached to circuits'
    version = '0.1'
    author = 'ds2600'
    author_email = 'ds2600@ds2600.com'
    base_url = 'circuit-docs'

    def ready(self):
        super().ready()

config = CircuitDocsConfig

class CircuitDocsExtension(PluginTemplateExtension):
    model = 'circuits.circuit'

    def reight_page(self):
        from .circuit_docs.models import CircuitDocument
        return self.render('netbox_circuit_docs/circuit_docs.html', extra_context={
            'documents': CircuitDocument.objects.filter(circuit=self.context['object']),
        })

template_extensions = [CircuitDocsExtension]

