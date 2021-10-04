import pytest
from base.models import Book
from django.test import Client
from rest_framework.test import APIClient
from faker import Faker

fake = Faker()


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def client_api():
    return APIClient()


title = 'book_title'
fake_author = fake.user_name()
fake_date = fake.date()
fake_isbn = fake.isbn13()
fake_num = fake.random_int(min=1, max=7000)
fake_img = fake.image_url()
fake_lang = fake.language_code()


@pytest.fixture
def book():
    return Book.objects.create(
        title=title,
        author=fake_author,
        publish_date=fake_date,
        ISBN=fake_isbn,
        num_of_pages=fake_num,
        cover_link=fake_img,
        publish_lang=fake_lang
    )


@pytest.fixture
def book_data():
    return {
        'title': 'title',
        'author': 'test',
        'publish_date': '2020-02-20',
        ' ISBN': '1234567890122',
        'num_of_pages': 650,
        'cover_link': 'https://www.google.com/',
        'publish_lang': 'en'
    }


@pytest.fixture
def books_fake_db():
    for _ in range(10):
        Book.objects.create(
            title=f'title{_}',
            author=fake_author,
            publish_date=fake_date,
            ISBN=fake_isbn,
            num_of_pages=fake_num,
            cover_link=fake_img,
            publish_lang=fake_lang
        )
    return Book.objects.all()
