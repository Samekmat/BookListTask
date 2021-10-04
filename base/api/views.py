from base.models import Book
from .serializers import BookSerializer
from rest_framework import generics
from django_filters import rest_framework as filters


class BookFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    author = filters.CharFilter(field_name='author', lookup_expr='icontains')
    publish_lang = filters.CharFilter(field_name='publish_lang', lookup_expr='icontains')
    start_date = filters.DateFilter(field_name='publish_date', lookup_expr='gte')
    end_date = filters.DateFilter(field_name='publish_date', lookup_expr='lte')

    class Meta:
        model = Book
        fields = ['title', 'author']


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BookFilter
