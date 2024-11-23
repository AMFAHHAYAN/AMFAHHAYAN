from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        exclude = ('created_at','updated_at')     
        labels = {
            'title': "Book Tittle", 
            'author': "Author Name", 
            'isbn': "isbn number", 
            'published_date': "Date of Published",
            'price': "Price ",
            'genre': "Book Genre(Type)",
            'language': "Book Language",
            'page_count': "Book Pages",
            'publisher': "Publisher Name",
            'is_bestseller': "Best Selling ",
            'stock_quantity': "Quantity",
        }
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'author': forms.TextInput(attrs={"class": "form-control"}),
            'published_date': forms.DateInput(attrs={"class": "form-control",'type':'date'}),
            'isbn': forms.TextInput(attrs={"class": "form-control"}),
            'price': forms.NumberInput(attrs={"class": "form-control"}),
            'genre': forms.TextInput(attrs={"class": "form-control"}),
            'language': forms.TextInput(attrs={"class": "form-control"}),  
            'page_count': forms.NumberInput(attrs={"class": "form-control"}),  
            'publisher': forms.TextInput(attrs={"class": "form-control"}),  
            'is_bestseller': forms.CheckboxInput(attrs={"class": "form-check-input"}),  
            'stock_quantity': forms.TextInput(attrs={"class": "form-control"}),  
        }

def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        super().__init__(*args, **kwargs)

        if instance:
            self.fields['isbn'].widget.attrs['readonly'] = True  
            self.fields['isbn'].required = False  
            del self.fields['isbn'] 