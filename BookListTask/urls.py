from django.contrib import admin
from django.urls import path
from base.views import index, add_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('add-book/', add_book, name='add-book'),
]
