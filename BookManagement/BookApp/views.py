from django.shortcuts import render,redirect,get_object_or_404
from .models import Book
from .forms import BookForm
from django.views import View
# Create your views here.


class Create(View):
    def get(self,request):
        form = BookForm()
        return render(request, "index.html", {'form':form})
    
    def post(self,request):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list') 
        return render(request, "index.html", {'form': form})
    
class List(View):
    def get(self,request):
        bookdata = Book.objects.all()
        return render(request,'list.html',{'data':bookdata})
    
class BookUpdate(View): 
    def get(self,request,id):
        book = Book.objects.get(id=id)
        form = BookForm(instance=book)
        return render(request,'index.html',{'form': form})
    def post(self,request,id):
        book = Book.objects.get(id=id)
        if request.method == 'POST':
            form = BookForm(request.POST, instance=book)
            if form.is_valid():
                form.save()
                return redirect('list')
        else:
            form = BookForm(instance=book)
            
        return render(request,'index.html',{'form': form})

class deletebook(View):
    def get(self,request,id):
        book = get_object_or_404( Book, id=id )
        book.delete()
        return redirect('list')
