from django.shortcuts import render, redirect
from .models import Kitab
from .forms import BookForm
from django.http import HttpResponse

# Create your views here.
def myfunc(request):
    if request.method == 'POST':
        print(request.POST)
        title = request.POST['title']
        price = request.POST.get('price')
        author = request.POST.get('author')
        edition = request.POST.get('edition')
        new_data = Kitab.objects.create(title=title, price=price, author=author, edition=edition)
        return redirect('base')
    return render(request, 'books.html')


def base(request):
    b = Kitab.objects.all
    return render(request, 'base.html', context={'books': b})



def djangoform(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        print(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            Kitab.objects.create(title=cleaned_data['title'],
                                 author=cleaned_data['author'],
                                 edition=cleaned_data['edition'],
                                 price=cleaned_data['price'])
            return redirect('base')
        else:
            return HttpResponse('Invalid Form Input')
    form = BookForm()  
    return render(request, 'djangoform.html', context={'form': form})