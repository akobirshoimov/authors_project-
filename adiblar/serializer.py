from rest_framework.serializers import ModelSerializer
from .models import AuthorModel,BooksModel,AuthorCategoryModel,BooksCategoryModel


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ('first_name','last_name','date_of_birth','date_of_death','where_be_born','where_die','description')

class BooksSerializer(ModelSerializer):
    class Meta:
        model = BooksModel
        fields = ('__all__')
    
class AuthorCategorySerializer(ModelSerializer):
    class Meta:
        model = AuthorCategoryModel
        fields = ('__all__')

class BooksCategorySerializer(ModelSerializer):
    class Meta:
        model = BooksCategoryModel
        fields = ('__all__')    

      
    
