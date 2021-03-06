from django.http.response import Http404
from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book
from .filters import BookFilter
import requests
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def index(request):
    return render(request, 'base.html')


def book_page(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        raise Http404('Book does not exist')
    return render(request, 'book.html', {'book': book})


def book_list(request):
    book_list = Book.objects.all()
    my_filter = BookFilter(request.GET, queryset=book_list)
    book_list = my_filter.qs

    page = request.GET.get('page', 1)
    paginator = Paginator(book_list, 6)

    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

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


def get_books(request):
    bulk_list = []
    books_found = {}
    url = f'https://www.googleapis.com/books/v1/volumes?q='
    if 'query' in request.GET:
        query = request.GET['query']
        url += query
        if 'titleS' in request.GET:
            title_s = request.GET['titleS']
            if title_s != '':
                url += f'+intitle:{title_s}'
        if 'authorS' in request.GET:
            author_s = request.GET['authorS']
            if author_s != '':
                url += f'+inauthor:{author_s}'
        if 'isbnS' in request.GET:
            isbn_s = request.GET['isbnS']
            if isbn_s != '':
                url += f'+isbn:{isbn_s}'

        if 'publisherS' in request.GET:
            publisher_s = request.GET['publisherS']
            if publisher_s != '':
                url += f'+inpublisher:{publisher_s}'

        if 'subjectS' in request.GET:
            subject_s = request.GET['subjectS']
            if subject_s != '':
                url += f'+subject:{subject_s}'

        if 'lccnS' in request.GET:
            lccn_s = request.GET['lccnS']
            if lccn_s != '':
                url += f'+lccn:{lccn_s}'

        if 'oclcS' in request.GET:
            oclc_s = request.GET['oclcS']
            if oclc_s != '':
                url += f'+isbn:{oclc_s}'

        response = requests.get(url)
        data = response.json()
        books_info = data['items']

        for book in books_info:
            try:
                title = ''
                authors = ''
                date = ''
                isbn = ''
                num_of_pg = ''
                cover = ''
                language = ''

                if book['volumeInfo']['title']:
                    title = book['volumeInfo']['title']

                if book['volumeInfo']['authors']:
                    authors = book['volumeInfo']['authors']

                if book['volumeInfo']['publishedDate']:
                    date = book['volumeInfo']['publishedDate']

                if book['volumeInfo']['industryIdentifiers']:
                    industry_identifiers = book['volumeInfo']['industryIdentifiers']

                    for id in industry_identifiers:
                        if id['type'] == 'ISBN_10' or id['type'] == 'ISBN_13':
                            isbn = id['identifier']
                        else:
                            isbn = ''

                if book['volumeInfo']['pageCount']:
                    num_of_pg = book['volumeInfo']['pageCount']

                if book['volumeInfo']['imageLinks']['thumbnail']:
                    cover = book['volumeInfo']['imageLinks']['thumbnail']

                if book['volumeInfo']['language']:
                    language = book['volumeInfo']['language']

                book_data = Book(
                    title=title,
                    author=authors,
                    publish_date=date,
                    ISBN=isbn,
                    num_of_pages=num_of_pg,
                    cover_link=cover,
                    publish_lang=language
                )
                bulk_list.append(book_data)
                books_found = Book.objects.all().order_by('-id')
            except KeyError:
                pass
            except Exception as e:
                print(e)
        Book.objects.bulk_create(bulk_list)
    return render(request, 'book_search.html', {'books_found': books_found})
