from django.shortcuts import render, redirect
from .models import Fornecedor, Contrato, Produto
from .forms import FornecedorForm, ProdutoForm, ContratoForm

def home(request):

    num_fornecedores = Fornecedor.objects.count()
    num_produtos = Produto.objects.count()
    num_contratos = Contrato.objects.count()
    
    context = {
        'num_fornecedores': num_fornecedores,
        'num_produtos': num_produtos,
        'num_contratos': num_contratos,
    }

    return render(request, 'core/home.html', context=context)

def cadastro_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FornecedorForm()

    return render(request, 'core/cadastro_fornecedor.html', {'form': form})

def cadastro_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProdutoForm()
    
    return render(request, 'core/cadastro_produto.html', {'form': form})

def cadastro_contrato(request):
    if request.method == 'POST':
        form = ContratoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContratoForm()
    
    return render(request, 'core/cadastro_contrato.html', {'form': form})