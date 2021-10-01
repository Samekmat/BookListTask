from django.contrib import admin
from django.urls import path
from base.views import index, add_book, book_list, book_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('add-book/', add_book, name='add-book'),
    path('books/', book_list, name='book-list'),
    path('book/<str:pk>/', book_page, name='book_page')
]
