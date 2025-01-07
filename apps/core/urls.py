from django.urls import path
from apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro_fornecedor/', views.cadastro_fornecedor, name='cadastro_fornecedor'),
    path('cadastro_produto/', views.cadastro_produto, name='cadastro_produto'),
    path('cadastro_contrato/<int:produto_id>/', views.cadastro_contrato, name='cadastro_contrato'),    
    path('listagem_produtos/', views.listagem_produtos, name='listagem_produtos'),
    path('detalhes_contrato/<int:contrato_id>/', views.detalhes_contrato, name='detalhes_contrato'),
    path('listagem_contratos/', views.listagem_contratos, name='listagem_contratos'),
]
