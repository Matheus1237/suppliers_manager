from django.urls import path
from apps.core import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('cadastro_fornecedor', views.cadastro_fornecedor, name='cadastro_fornecedor'),
    path('cadastro_produto', views.cadastro_produto, name='cadastro_produto'),
    path('cadastro_contrato', views.cadastro_contrato, name='cadastro_contrato')
]
