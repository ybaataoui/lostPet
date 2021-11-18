from django.shortcuts import render
from django.http import request
from .models import Pet


def index(request):
    pets = [
        {'title' : 'First Pet', 'location' : 'New York', 'slug' : 'a-first-pet'},
        {'title' : 'Second Pet', 'location' : 'Florida', 'slug' : 'a-secon-pet'}
    ]
    return render(request, 'pets/index.html', {
        'show_pets' : True,
        'pets': pets 
        })

def pet_details(request, pet_slug):
    selected_pet = { 'title' : 'First pets', 'description' : 'This is my first pet'}
    
    return render(request, 'pets/pet_details.html', { 
        'pet_title' : selected_pet['title'],
        'pet_description' : selected_pet['description']
    })

def pet_input(request):
    return render(request, 'pets/input.html', {})

def all_pets(request):
    pet_list = Pet.objects.all()
    return render(request, 'pets/pet_list.html', 
        { 'pet_list' : pet_list })