from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import PROTECT


class PetOwner(models.Model):
    first_name = models.CharField(max_length=255)
    last_name  = models.CharField(max_length=255)
    phone      = models.CharField(max_length=255)
    email      = models.EmailField(unique=True)


class PetCategory(models.Model):
    name = models.CharField(max_length=255)

class Species(models.Model):
    name = models.CharField(max_length=255)

class Color(models.Model):
    name = models.CharField(max_length=255)

class Breed(models.Model):
    name = models.CharField(max_length=255)

class State(models.Model):
    name = models.CharField(max_length=255)

class Address(models.Model):
    street   = models.CharField(max_length=255)
    city     = models.CharField(max_length=255)
    zip_code = models.PositiveIntegerField()
    state    = models.ForeignKey(State, on_delete=models.PROTECT)

class Employee(models.Model):
    USER_ADMIN   = 'A'
    USER_REGULAR = 'R'

    USER_TYPE = [
        (USER_ADMIN, 'Admin'),
        (USER_REGULAR, 'Regular')
    ]

    first_name = models.CharField(max_length=255)
    last_name  = models.CharField(max_length=255)
    phone      = models.CharField(max_length=255)
    email      = models.EmailField(unique=True)
    username   = models.CharField(max_length=255)
    password   = models.CharField(max_length=255)
    type       = models.CharField(max_length=1, choices=USER_TYPE, default=USER_REGULAR)
    address    = models.ForeignKey(Address, on_delete=models.CASCADE)

class Pet(models.Model):
    PET_FEMALE = 'F'
    PET_MALE   = 'M'
    PET_SPAYED = 'S'
    PET_NEUTRED = 'N'
    PET_NO      = 'O'

    FIXED_CHOICES = [ 
        (PET_SPAYED, 'Spayed'),
        (PET_NEUTRED, 'Neutred'),
        (PET_NO, 'No')
    ]


    GENDER_CHOICES = [ 
        (PET_FEMALE, 'FEMALE'),
        (PET_MALE, 'MALE')
    ]

    body_color  = models.ForeignKey('Color', on_delete=models.PROTECT)
    eye_color   = models.ForeignKey('Color', on_delete=models.PROTECT, related_name='color')
    description = models.CharField(max_length=255)
    picture     = models.ImageField()
    gender      = models.CharField(max_length=1, choices=GENDER_CHOICES)
    fixed       = models.CharField(max_length=1, choices=FIXED_CHOICES, default=PET_NO)
    category    = models.ForeignKey(PetCategory, on_delete=models.PROTECT )
    breed       = models.ForeignKey(Breed, on_delete=models.PROTECT )
    species     = models.ForeignKey(Species, on_delete=models.PROTECT )

class Input(models.Model):
    INPUT_LOST = 'L'
    INPUT_FOUND = 'F'

    INPUT_CHOICES = [ 
        (INPUT_LOST, 'Lost'),
        (INPUT_FOUND, 'Found')
    ]


    input_type = models.CharField(max_length=1, choices=INPUT_CHOICES)
    date_created = models.DateField(auto_now_add=True)
    date_lost    = models.DateField()
    date_found   = models.DateField(null=True)
    owner        = models.ForeignKey(PetOwner, on_delete=models.CASCADE)
    address      = models.ForeignKey(Address, on_delete=models.CASCADE)
    employee     = models.ForeignKey(Employee, on_delete=models.PROTECT)
    pet          = models.ForeignKey(Pet, on_delete=models.CASCADE)





