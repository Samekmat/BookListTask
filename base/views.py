from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book


def index(request):
    return render(request, 'index.html')


def book_page(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'book.html', {'book': book})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def add_book(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    ctx = {'form': form}
    return render(request, 'book_form.html', ctx)
