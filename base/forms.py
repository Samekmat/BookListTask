from django.forms import ModelForm, TextInput
from .models import Book


STYLE = {'class': 'input is-dark is-rounded is-large is-info'}


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs=STYLE),
            'author': TextInput(attrs=STYLE),
            'publish_date': TextInput(attrs=STYLE),
            'ISBN': TextInput(attrs=STYLE),
            'num_of_pages': TextInput(attrs=STYLE),
            'cover_link': TextInput(attrs=STYLE),
            'publish_lang': TextInput(attrs=STYLE)
        }
