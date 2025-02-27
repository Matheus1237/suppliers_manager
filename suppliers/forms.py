from django import forms
from .models import Fornecedor, Produto, Contrato

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome', 'telefone', 'email', 'cidade', 'estado', 'cep']
        widgets = {
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cidade'}),
            'estado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estado (UF)'}),
            'cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CEP'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Fornecedor'}),
        }

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['produto', 'fornecedor', 'valor_por_unidade']
        widgets = {
            'produto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Produto'}),
            'fornecedor': forms.Select(attrs={'class': 'form-control'}),
            'valor_por_unidade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Valor por Unidade', 'step': '0.01'}),
        }

class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ['produto', 'quantidade']
        widgets = {
            'produto': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade', 'min': '1'}),
        }