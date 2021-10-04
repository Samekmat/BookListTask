from django.urls import resolve, reverse
from base.views import index, book_page, book_list, add_book, update_book, delete_book, get_books
import pytest


def test_index_view(client):
    url = reverse('index')
    found = resolve(url)
    resp = client.get(url)
    assert found.func == index
    assert resp.status_code == 200


@pytest.mark.django_db
def test_book_page_view(client, book):
    resp = client.get(f'/book/{book.id}/')
    found = resolve(reverse('book_page', kwargs={'pk': book.id}))
    assert resp.status_code == 200
    assert found.func == book_page
    assert book.title == 'book_title'


@pytest.mark.django_db
def test_book_list_view(client, books_fake_db):
    url = reverse('book-list')
    books = books_fake_db
    resp = client.get(url)
    found = resolve(url)
    assert resp.status_code == 200
    assert books.count() == 10
    assert found.func == book_list


@pytest.mark.django_db
def test_book_add(client, book_data):
    response = client.post('/add-book/', book_data)
    found = resolve(reverse('add-book'))
    assert response.status_code == 302
    assert found.func == add_book


@pytest.mark.django_db
def test_book_update(client, books_fake_db, book_data):
    book = books_fake_db.first()
    resp = client.post(f'/update-book/{book.id}/', book_data)
    found = resolve(reverse('update-book', kwargs={'pk': book.id}))
    assert resp.status_code == 302
    assert found.func == update_book


@pytest.mark.django_db
def test_book_delete(client, books_fake_db):
    book = books_fake_db.first()
    found = resolve(reverse('delete-book', kwargs={'pk': book.id}))
    resp = client.get(f'/delete-book/{book.pk}/')
    assert resp.status_code == 200
    resp = client.post(f'/delete-book/{book.pk}/')
    assert resp.status_code == 302
    assert found.func == delete_book


def test_get_books(client, book_data):
    url = reverse('get-books')
    found = resolve(url)
    resp = client.get(url)
    assert resp.status_code == 200
    assert found.func == get_books


@pytest.mark.django_db
def test_book_list_api(client_api):
    url = '/api/'
    resp_get = client_api.get(url)
    assert resp_get.status_code == 200
    resp_post = client_api.post(url)
    assert resp_post.status_code == 405
    resp_put = client_api.put(url)
    assert resp_put.status_code == 405
    resp_delete = client_api.delete(url)
    assert resp_delete.status_code == 405
    resp_patch = client_api.patch(url)
    assert resp_patch.status_code == 405
    resp_options = client_api.options(url)
    assert resp_options.status_code == 200
    resp_head = client_api.head(url)
    assert resp_head.status_code == 200
    resp_trace = client_api.trace(url)
    assert resp_trace.status_code == 405
