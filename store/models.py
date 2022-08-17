from django.db import models

class Categoria(models.Model):
  nome = models.CharField(max_length=150)

  def __str__(self):
    return self.nome

class Produto(models.Model):
  nome = models.CharField('Nome do produto', max_length=150)
  preco = models.DecimalField('Preço do produto:', max_digits=8, decimal_places=2)
  imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
  categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
  descricao = models.TextField('Descrição do produto:')

  def __str__(self):
    return self.nome

