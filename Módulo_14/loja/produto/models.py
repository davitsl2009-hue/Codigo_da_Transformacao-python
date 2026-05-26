from django.db import models

class Produto(models.Model):
    
    nome = models.CharField(max_length=128, verbose_name="Nome do Produto")
    
    descricao = models.TextField(verbose_name="Descrição", blank=True, null=True)
    
    preco = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Preço")
    
    quantidade = models.IntegerField(verbose_name="Quantidade em Estoque")

    def __str__(self):
        return self.nome