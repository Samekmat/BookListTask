from django.urls import path
from base.api.views import get_books

urlpatterns = [
    path('', get_books)
]
