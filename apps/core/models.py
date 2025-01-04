from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)

    # Endereço
    cidade = models.CharField(max_length=255, blank=True)
    estado = models.CharField(max_length=2, blank=True)
    cep = models.CharField(max_length=10, blank=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"

class Produto(models.Model):
    produto = models.CharField(max_length=255)
    fornecedor = models.ForeignKey(Fornecedor, related_name='produtos', on_delete=models.CASCADE)
    valor_por_unidade = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.produto} - {self.fornecedor.nome}"
    
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"    

class Contrato(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        return f"Contrato de {self.quantidade} unidades de {self.produto.produto}"

    class Meta:
        verbose_name = "Contrato"
        verbose_name_plural = "Contratos"