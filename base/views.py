from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book
from .filters import BookFilter


def index(request):
    return render(request, 'base.html')


def book_page(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'book.html', {'book': book})


def book_list(request):
    books = Book.objects.all()
    my_filter = BookFilter(request.GET, queryset=books)
    books = my_filter.qs
    ctx = {'books': books, 'filter': my_filter}
    return render(request, 'book_list.html', ctx)


def add_book(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    ctx = {'form': form}
    return render(request, 'book_form.html', ctx)


def update_book(request, pk):
    book = Book.objects.get(pk=pk)
    form = BookForm(request.POST)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    return render(request, 'book_form.html', {'form': form})


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book-list')
    return render(request, 'book_delete.html', {'obj': book})
