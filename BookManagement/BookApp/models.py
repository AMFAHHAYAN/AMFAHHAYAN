from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)#random
    price = models.DecimalField(max_digits=6, decimal_places=2)
    genre = models.CharField(max_length=50, null=True, blank=True) # Genre of the book
    language = models.CharField(max_length=50, default="English") # Language of the book
    page_count = models.PositiveIntegerField(null=True, blank=True) 
    publisher = models.CharField(max_length=255, null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True) # Timestamp for creation
    updated_at = models.DateTimeField(auto_now=True) # Timestamp for updates
    is_bestseller = models.BooleanField(default=False) # Bestseller status
    stock_quantity = models.PositiveIntegerField(default=0) # Quantity in stock
    
    
    def __str__(self):
        return f"{self.title} by {self.author}"