from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Sale(models.Model):
    product = models.ForeignKey('books.Product', on_delete=models.CASCADE)
    quantity_sold = models.PositiveIntegerField()
    sale_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.product.quantity -= self.quantity_sold
        self.product.save()
        super(Sale, self).save(*args, **kwargs)