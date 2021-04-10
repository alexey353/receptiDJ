from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('create-recipes', views.create_recipes, name='create-recipes'),
    path('zakuski', views.zakuski, name='zakuski'),
    path('main-dish', views.main_dish, name='main-dish'),
    path('salads', views.salads, name='salads'),
    path('desserts', views.desserts, name='desserts'),
    path('drinks', views.drinks, name='drinks'),
    path('vegetarians', views.vegetarians, name='vegetarians'),
    path('<int:pk>', views.RecipesDetailView.as_view(), name='recept-detail')
]
