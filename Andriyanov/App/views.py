from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import (ListCreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView,
                                     RetrieveUpdateDestroyAPIView, CreateAPIView)
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny
from rest_framework.views import APIView
from .models import *
from .serializers import *

####### Films #######
class ListFilms(ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializers
    permission_classes = [AllowAny]

class CreateFilms(ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = DetailFilmSerializers
    permission_classes = [IsAdminUser]

class DetailFilms(RetrieveAPIView):
    queryset = Film.objects.all()
    serializer_class = DetailFilmSerializers
    permission_classes = [AllowAny]

class CRUDFilms(RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = DetailFilmSerializers
    permission_classes = [IsAdminUser]


####### Reviews #######
class ListReviews(ListAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers
    permission_classes = [AllowAny]

class CreateReviews(CreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers
    permission_classes = [IsAdminUser]

class CRUDReviews(RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers
    permission_classes = [IsAdminUser]

####### Actors #######
class ListActors(ListAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializers
    permission_classes = [AllowAny]

class CreateActors(CreateAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializers
    permission_classes = [IsAdminUser]

class CRUDActors(RetrieveUpdateDestroyAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializers
    permission_classes = [IsAdminUser]

####### Category #######
class ListCategory(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [AllowAny]

class CreateCategory(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsAdminUser]

class CRUDCategory(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsAdminUser]

####### Genres #######
class ListGenres(ListAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializers
    permission_classes = [AllowAny]

class CreateGenres(CreateAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializers
    permission_classes = [IsAdminUser]

class CRUDGenres(RetrieveUpdateDestroyAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializers
    permission_classes = [IsAdminUser]