from django import forms
from ..models import Book

class BookForm(forms.ModelForm):
    title = forms.CharField()
    author = forms.CharField()

    class Meta:
        model = Book
        fields = '__all__'
    def save(self, commit=True):
        instance = super(BookForm, self).save(commit=False)
        instance.save()
        return instance