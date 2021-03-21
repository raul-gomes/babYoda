from django.db import models

# Create your models here.

class Item(models.Model):
    item = models.CharField(max_length=200)
    preco = models.FloatField()
    quantidade = models.IntegerField()
    imagem = models.ImageField(upload_to='chaFraldas')
    data_criacao = models.DateField(auto_now=True)

    def __str__(self):
        return self.item
