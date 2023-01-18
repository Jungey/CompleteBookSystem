from django.shortcuts import render, redirect
from .forms import DjangoForm
from .models import Pustak

# Create your views here.
def addbook(request):
    if request.method == 'POST':
        form_data = DjangoForm(request.POST)
        if form_data.is_valid():
            title = request.POST['title']
            author = request.POST.get('author')
            edition = request.POST['edition']
            price = request.POST['price']
            Pustak.objects.create(title=title, author=author, edition=edition, price=price)
            return redirect('home')
    form = DjangoForm()
    return render(request, 'djangoForm/book.html', context={'forms': form})


def home(request):
    book_data = Pustak.objects.all()
    return render(request, 'djangoForm/base.html', context={'booklist': book_data})