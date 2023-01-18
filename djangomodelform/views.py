from django.shortcuts import render, redirect
from .forms import BookModelForm
from .models import Granth

# Create your views here.

def bookthap(request):
    if request.method == 'POST':
        form_data = BookModelForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('base')
    form = BookModelForm()
    return render(request, 'djangomodelform/book.html', context={'form': form})


def base(request):
    booklist = Granth.objects.all()
    return render(request, 'djangomodelform/base.html', context={'booklist': booklist})