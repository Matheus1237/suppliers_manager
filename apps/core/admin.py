from django.contrib import admin
from .models import Fornecedor, Produto, Contrato

class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email', 'cidade', 'estado', 'cep')
    search_fields = ('nome', 'telefone', 'email', 'cidade', 'estado', 'cep')

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'fornecedor')
    search_fields = ('produto', 'fornecedor')

class ContratoAdmin(admin.ModelAdmin):
    list_display = ['produto', 'quantidade']
    search_fields = ['produto', 'quantidade']

admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Contrato, ContratoAdmin)