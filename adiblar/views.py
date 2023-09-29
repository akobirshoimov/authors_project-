from django.shortcuts import render,get_object_or_404
from .models import AuthorModel,BooksModel,BooksCategoryModel,AuthorCategoryModel
from rest_framework  import generics
from rest_framework.permissions import IsAuthenticated
from .serializer import AuthorSerializer,BooksSerializer,BooksCategorySerializer,AuthorCategorySerializer
from .permission import AdminPermisson,StaffPermisson
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

#Author CRUD 

class CreateAuthorView(generics.CreateAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticated,AdminPermisson)


class ListAuthorView(generics.ListAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticated,)

class UpdateAuthorView(generics.UpdateAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticated,StaffPermisson)

class DeleteAuthorView(generics.DestroyAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticated,AdminPermisson)

#Books CRUD

class CreateBooksView(generics.CreateAPIView):
    queryset = BooksModel.objects.all()
    serializer_class = BooksSerializer
    permission_classes = (IsAuthenticated,AdminPermisson)

class ListBooksView(generics.ListAPIView):
    queryset = BooksModel.objects.all()
    serializer_class = BooksSerializer
    permission_classes = (IsAuthenticated,)

class UpdateBooksView(generics.UpdateAPIView):
    queryset = BooksModel.objects.all()
    serializer_class = BooksSerializer
    permission_classes = (IsAuthenticated,StaffPermisson)


class DeleteBooksView(generics.DestroyAPIView):
    queryset = BooksModel.objects.all()
    serializer_class = BooksSerializer
    permission_classes = (IsAuthenticated,AdminPermisson)

#BooksCategory CRUD

class CreateBooksCategoryView(generics.CreateAPIView):
    queryset = BooksCategoryModel.objects.all()
    serializer_class = BooksCategorySerializer
    permission_classes = (IsAuthenticated,AdminPermisson)

class ListBooksCategoryView(generics.ListAPIView):
    queryset = BooksCategoryModel.objects.all()
    serializer_class = BooksCategorySerializer
    permission_classes = (IsAuthenticated,)

class UpdateBooksCategoryView(generics.UpdateAPIView):
    queryset = BooksCategoryModel.objects.all()
    serializer_class = BooksCategorySerializer
    permission_classes = (IsAuthenticated,StaffPermisson)


class DeleteBooksCategoryView(generics.DestroyAPIView):
    queryset = BooksCategoryModel.objects.all()
    serializer_class = BooksCategorySerializer
    permission_classes = (IsAuthenticated,AdminPermisson)

#AuthorCategory CRUD

class CreateAuthorCategoryView(generics.CreateAPIView):
    queryset = AuthorCategoryModel.objects.all()
    serializer_class = AuthorCategorySerializer
    permission_classes = (IsAuthenticated,AdminPermisson)

class ListAuthorCategoryView(generics.ListAPIView):
    queryset = AuthorCategoryModel.objects.all()
    serializer_class =AuthorCategorySerializer
    permission_classes = (IsAuthenticated,)

class UpdateAuthorCategoryView(generics.UpdateAPIView):
    queryset = AuthorCategoryModel.objects.all()
    serializer_class = AuthorCategorySerializer
    permission_classes = (IsAuthenticated,StaffPermisson)


class DeleteAuthorCategoryView(generics.DestroyAPIView):
    queryset = AuthorCategoryModel.objects.all()
    serializer_class = AuthorCategorySerializer
    permission_classes = (IsAuthenticated,AdminPermisson)


        

    












