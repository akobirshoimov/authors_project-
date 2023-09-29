from django import forms
from adiblar.models import BooksModel,BooksCategoryModel,AuthorModel,AuthorCategoryModel


class BooksForm(forms.ModelForm):
    name_uz = forms.CharField()
    name_en = forms.CharField()
    name_ru = forms.CharField()

    desc_uz = forms.CharField()
    desc_en = forms.CharField()
    desc_ru = forms.CharField()

    class Meta:
        model = BooksModel
        exclude = ('name', 'description')

class AuthorForm(forms.ModelForm):
    desc_uz = forms.CharField()
    desc_en = forms.CharField()
    desc_ru = forms.CharField()

    class Meta:
        model = AuthorModel
        exclude = ('description',)

class BooksCategoryForm(forms.ModelForm):
    name_uz = forms.CharField()
    name_en = forms.CharField()
    name_ru = forms.CharField()

    book_uz = forms.CharField()
    book_en = forms.CharField()
    book_ru = forms.CharField()

    class Meta:
        model = BooksCategoryModel
        exclude = ('name', 'book')

class AuthorCategoryForm(forms.ModelForm):
    name_uz = forms.CharField()
    name_en = forms.CharField()
    name_ru = forms.CharField()

    class Meta:
        model = AuthorCategoryModel
        exclude = ('name',)

