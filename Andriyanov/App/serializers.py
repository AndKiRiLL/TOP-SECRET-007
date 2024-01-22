from rest_framework import serializers
from .models import *


class ReviewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = "__all__"

class FilmSerializers(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('title','year','country')

class DetailFilmSerializers(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = "__all__"


class ActorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actors
        fields = "__all__"

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class GenresSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = "__all__"