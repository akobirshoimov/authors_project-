from django.contrib import admin
from .models import AuthorModel,BooksModel,BooksCategoryModel,AuthorCategoryModel
# Register your models here.

admin.site.register(AuthorModel)
admin.site.register(BooksModel)
admin.site.register(BooksCategoryModel)
admin.site.register(AuthorCategoryModel)