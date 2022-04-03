from django.shortcuts import render,redirect
from .models import Books
from .addbook import BooksForm
 
# Create your views here.

def getBookslist(request):
    
    books= Books.objects.all()
    form = BooksForm(request.POST)
    if request.method == 'POST':
        form= BooksForm(request.POST)
        if form.is_valid():
            form.save()
    contex={'books':books,'form':form} 
    return render(request, "market.html",contex)

def deleteBook(request,pk):
    book= Books.objects.get(id=pk)
    
    book.delete()
    return redirect('market')
   
    

#def addBook(request):
    ##form= BooksForm()
    
    #if request.method=='POST':
       # form = BooksForm(request.POST)
       # if form.is_valid:
        #    form.save()
          #  return.return