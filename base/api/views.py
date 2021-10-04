from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Book


@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    return Response(books)
