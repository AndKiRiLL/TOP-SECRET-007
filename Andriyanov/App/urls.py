from django.urls import path, re_path, include
from .views import *

urlpatterns = [

    path('films/', ListFilms.as_view()),
    path('films/create/', CreateFilms.as_view()),
    path('films/<int:pk>/', DetailFilms.as_view()),
    path('films/crud/<int:pk>/', CRUDFilms.as_view()),

    path('reviews/', ListReviews.as_view()),
    path('reviews/create/', CreateReviews.as_view()),
    path('reviews/crud/<int:pk>/', CRUDReviews.as_view()),

    path('actors/', ListActors.as_view()),
    path('actors/create/', CreateActors.as_view()),
    path('actors/crud/<int:pk>/', CRUDActors.as_view()),

    path('category/', ListCategory.as_view()),
    path('category/create/', CreateCategory.as_view()),
    path('category/crud/<int:pk>/', CRUDCategory.as_view()),

    path('genres/', ListGenres.as_view()),
    path('genres/create/', CreateGenres.as_view()),
    path('genres/crud/<int:pk>/', CRUDGenres.as_view()),

]