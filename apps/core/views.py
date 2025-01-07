from django.shortcuts import render, redirect, get_object_or_404
from .models import Fornecedor, Contrato, Produto
from .forms import FornecedorForm, ProdutoForm
from django.contrib import messages

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

def cadastro_contrato(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    
    if request.method == "POST":
        quantidade = request.POST.get("quantidade")
        if quantidade.isdigit():
            quantidade = int(quantidade)
            contrato = Contrato.objects.create(produto=produto, quantidade=quantidade)
            messages.success(request, "Contrato criado com sucesso!")
            
            # Redireciona para os detalhes do contrato recém-criado
            return redirect('detalhes_contrato', contrato_id=contrato.id)
        else:
            messages.error(request, "A quantidade deve ser um número válido.")
    
    return render(request, 'core/cadastro_contrato.html', {'produto': produto})

def listagem_produtos(request):

    produtos = Produto.objects.all()

    return render(request, 'core/listagem_produtos.html', {'produtos': produtos})

def detalhes_contrato(request, contrato_id):

    contrato = get_object_or_404(Contrato, id=contrato_id)
    valor_total = contrato.produto.valor_por_unidade * contrato.quantidade

    return render(request, 'core/detalhes_contrato.html', {'contrato': contrato, 'valor_total': valor_total})

def listagem_contratos(request):

    contratos = Contrato.objects.all()

    for contrato in contratos:
        contrato.valor_total = contrato.produto.valor_por_unidade * contrato.quantidade

    return render(request, 'core/listagem_contratos.html', {'contratos': contratos})