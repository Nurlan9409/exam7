from django.db import models
from users.models import User
class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='category/category/')
    watched = models.PositiveSmallIntegerField(default=0)
    create_date = models.DateTimeField(auto_now=True)
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.watched} - {self.description}"


class Product(models.Model):

    class PriceType(models.TextChoices):
        sum = "Sum", "sum"

    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='category/product/')
    description = models.TextField()
    price = models.FloatField()
    remaining = models.PositiveSmallIntegerField()
    reyting = models.FloatField(default=0)
    price_type = models.CharField(max_length=10, choices=PriceType.choices, default=PriceType.sum, null=True)
    category = models.ManyToManyField(Category)
    buy_count = models.PositiveBigIntegerField(default=0)
    create_date = models.DateTimeField(auto_now=True)
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.price_type} - {self.price}  {self.category} "

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    create_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'Review by {self.product} on {self.comment}'



class Search(models.Model):
    field = models.CharField(max_length=100)

    def __str__(self):
        return self.field