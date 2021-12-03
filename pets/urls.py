from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    #path('pets/<slug:pet_slug>', views.pet_details, name="pet-detail"),
    path('pets/', views.add_pet, name="add-pet"),
    path('pets_list/', views.all_pets, name="list_pets"),
    path('FAQ/', views.faqpage, name="FAQ"),
    path('about/', views.about, name="about"),
    path('login/', views.login, name="login"),
    path('owner/', views.owner, name="add-owner"), 
    path('add_employee/', views.add_employee, name='add_employee'), 

]