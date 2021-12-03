
from django.core.checks import messages
from django.shortcuts import render
from django.http import request
from .models import Pet, PetOwner, Employee
from .forms import PetForm, PetOwnerForm, EmployeeForm
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages



def home(request):
    return render(request, 'pets/home.html', {})

def pet_details(request, pet_slug):
    selected_pet = { 'title' : 'First pets', 'description' : 'This is my first pet'}
    
    return render(request, 'pets/pet_details.html', { 
        'pet_title' : selected_pet['title'],
        'pet_description' : selected_pet['description']
    })



def all_pets(request):
    pet_list = Pet.objects.all()
    return render(request, 'pets/pets-list.html', 
        { 'pet_list' : pet_list })


def faqpage(request):
    return render(request, 'pets/FAQpage.html')

def about(request):
    return render(request, 'pets/about.html')

def login(request):
    return render(request, 'pets/login.html')

def owner(request):
    
    submitted = False
    if request.method == "POST":
        form = PetOwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/owner?submitted=True')
    else:
        form = PetOwnerForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request,'pets/owner.html', {'form': form, 'submitted': submitted } )

def pet_input(request):
    submitted = False
    if request.method == "POST":
        
        form = PetForm(request.POST)
        print('saved')
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/pets?submitted=True')
    else:
        form = PetForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'pets/new_pet.html', { 'form': form, 'submitted': submitted })


def add_employee(request):
    if request.method == "POST":
        type = EmployeeForm(request.POST)
        addemployee = Employee()
        addemployee.first_name=request.POST.get('first_name')
        addemployee.last_name=request.POST.get('last_name')
        addemployee.phone=request.POST.get('phone')
        addemployee.email=request.POST.get('email')
        addemployee.username=request.POST.get('username')
        addemployee.password=request.POST.get('password')
        addemployee.type=request.POST.get('type')
        addemployee.street=request.POST.get('street')
        addemployee.city=request.POST.get('city')
        addemployee.zip_code=request.POST.get('zip_code')
        addemployee.state=request.POST.get('state')
        addemployee.save()
        messages.success(request, 'Employee ' + addemployee.first_name + ' ' + addemployee.last_name + ' is add Successfully...!')
        
        return render(request, 'pets/employee-form.html', {'type': type})
    else:
        return render(request, 'pets/employee-form.html')


def add_pet(request):

    if request.method == "POST":
        pet = Pet()
        owner = PetOwner()

        pet.date_lost = request.POST.get('date')
        pet.pet_type = request.POST.get('pettype')
        pet.species = request.POST.get('species')
        pet.breed = request.POST.get('breed')
        pet.gender = request.POST.get('gender')
        pet.eye_color = request.POST.get('eyecolor')
        pet.body_color = request.POST.get('bodycolor')
        pet.fixed = request.POST.get('fixed')
        pet.picture = request.POST.get('petphoto')
        pet.street = request.POST.get('location')
        pet.city = request.POST.get('city')
        pet.state = request.POST.get('state')
        pet.zip_code = request.POST.get('zip')
        owner.first_name = request.POST.get('fname')
        owner.last_name = request.POST.get('lname')
        owner.phone = request.POST.get('phone')
        owner.email = request.POST.get('email')
        pet.description = request.POST.get('description')
        pet.save()
        owner.save()

        return render(request, 'pets/add_pet.html')
    else:
        return render(request, 'pets/add_pet.html')











