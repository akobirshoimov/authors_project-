from django.db import models

# Create your models here.

class AuthorModel(models.Model):
    first_name = models.CharField(max_length=50,default=' ')
    last_name = models.CharField(max_length=50,default=' ')
    date_of_birth = models.DateField(default='1945-08-02')
    date_of_death = models.DateField(default='2000-02-03')
    where_be_born = models.CharField(max_length=100,default=' ')
    where_die = models.CharField(max_length=100,default=' ')
    description = models.TextField(default=' ')

    def __str__(self) -> str:
        return f'{self.first_name}  {self.last_name} '
    
class BooksModel(models.Model):
    name = models.CharField(max_length=100,default=' ')
    pages = models.IntegerField(default=200)
    publication_date = models.DateField(default='2004-10-02')
    price = models.CharField(max_length=100)
    author = models.ForeignKey(AuthorModel,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class AuthorCategoryModel(models.Model):
    name = models.CharField(max_length=60)
    author = models.ForeignKey(AuthorModel,on_delete=models.CASCADE)
    

    def __str__(self) -> str:
        return self.name
class BooksCategoryModel(models.Model):
    name = models.CharField(max_length=80)
    book = models.ForeignKey(BooksModel,on_delete=models.CASCADE)
    