from django.urls import path
from .views import (ListAuthorView,CreateAuthorView,UpdateAuthorView,DeleteAuthorView,
                    ListBooksView,CreateBooksView,UpdateBooksView,DeleteBooksView,
                    ListAuthorCategoryView,CreateAuthorCategoryView,UpdateAuthorCategoryView,DeleteAuthorCategoryView,
                    ListBooksCategoryView,CreateBooksCategoryView,UpdateBooksCategoryView,DeleteBooksCategoryView,
                    )


urlpatterns = [
    #author
    path('createAuthor',CreateAuthorView.as_view()),
    path('allAuthor/',ListAuthorView.as_view()),
    path('updateAuthor/<int:pk>/',UpdateAuthorView.as_view()),
    path('deleteAuthor/<int:pk>/',DeleteAuthorView.as_view()),
    #books
    path('createBooks/',CreateBooksView.as_view()),
    path('allBooks/',ListBooksView.as_view()),
    path('updateBooks/<int:pk>/',UpdateBooksView.as_view()),
    path('deleteBooks/<int:pk>/',DeleteBooksView.as_view()),
    #BooksCategory
    path('createBooksCategory',CreateBooksCategoryView.as_view()),
    path('allBooksCategory/',ListBooksCategoryView.as_view()),
    path('updateBooksCategory/<int:pk>/',UpdateBooksCategoryView.as_view()),
    path('deleteBooksCategory/<int:pk>/',DeleteBooksCategoryView.as_view()),
    #AuthorCategory
    path('createAuthorCategory/',CreateAuthorCategoryView.as_view()),
    path('allAuthorCategory/',ListAuthorCategoryView.as_view()),
    path('updateAuthorCategory/<int:pk>',UpdateAuthorCategoryView.as_view()),
    path('deleteAuthorCategory/<int:pk>',DeleteAuthorCategoryView.as_view()),
    
    
]