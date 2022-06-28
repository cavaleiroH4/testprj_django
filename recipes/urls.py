from django.urls import path

from . import views

urlpatterns = [

    path('', views.home, name="home_recipe"),
    path('recipes/<int:id>/', views.recipe, name="recipes_recipe"),
]
