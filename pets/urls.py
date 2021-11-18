from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="all-pets"),
    path('pets/<slug:pet_slug>', views.pet_details, name="pet-detail"),
    path('pets/', views.pet_input, name="add_pet"),
    path('templates/pets/', views.all_pets, name="list_pets"),

]