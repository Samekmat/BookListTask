from django.shortcuts import render, redirect
from .forms import BookForm


def index(request):
    return render(request, 'index.html')


def add_book(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    ctx = {'form': form}
    return render(request, 'book_form.html', ctx)
