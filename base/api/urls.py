from django.urls import path
from base.api.views import BookList

urlpatterns = [
    path('', BookList.as_view()),
]
