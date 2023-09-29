from modeltranslation.translator import translator,TranslationOptions
from adiblar.models import BooksCategoryModel,AuthorCategoryModel,BooksModel,AuthorModel

class BooksCategoryTranslation(TranslationOptions):
    fields = ('name','book')
    required_languages = 'uz'

class AuthorCategoryTranslation(TranslationOptions):
    fields = ('name',)
    required_languages = 'en'

class BooksTranslation(TranslationOptions):
    fields = ('name',' description')
    required_languages = 'ru'

class AuthorTranslation(TranslationOptions):
    fields = ('description',)
    required_languages = 'uz'
