from django.db import models
class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/category')
    watched = models.PositiveSmallIntegerField(default=0)
    create_date = models.DateTimeField(auto_now=True)
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

class Product(models.Model):

    class PriceType(models.TextChoices):
        sum = "Sum", "sum"

    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='category/product/')
    description = models.TextField()
    price = models.FloatField()
    made_in = models.CharField(max_length=50)
    price_type = models.CharField(max_length=10, choices=PriceType.choices, default=PriceType.sum, null=True)
    category = models.ManyToManyField(Category)
    buy_count = models.PositiveBigIntegerField(default=0)
    create_date = models.DateTimeField(auto_now=True)
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.price_type} - {self.price}  {self.category} "
