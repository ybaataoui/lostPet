from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import PROTECT
from django import forms
from django.db.models.fields import DateField
from django.forms import widgets
from django.utils import timezone



class PetOwner(models.Model):
    first_name = models.CharField(max_length=255)
    last_name  = models.CharField(max_length=255)
    phone      = models.CharField(max_length=255)
    email      = models.EmailField(unique=True)

    def __str__(self):
        return self.first_name 

class Species(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

#class Color(models.Model):
    #name = models.CharField(max_length=255)

    #def __str__(self):
        #return self.name

class Breed(models.Model):
    name = models.CharField(max_length=255)
    species = models.ForeignKey(Species, on_delete=models.PROTECT,  blank=True)

    def __str__(self):
        return self.name + ' ' + self.species.name

#class State(models.Model):
    #name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

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
    type       = models.CharField(max_length=255, choices=USER_TYPE)
    street     = models.CharField(max_length=255)
    city       = models.CharField(max_length=255)
    zip_code   = models.CharField(max_length=15)
    state      = models.CharField(max_length=30, default='Florida')
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Pet(models.Model):
    PET_FEMALE = 'F'
    PET_MALE   = 'M'
    GENDER_CHOICES = [ (PET_FEMALE, 'FEMALE'), (PET_MALE, 'MALE')]

    PET_SPAYED = 'S'
    PET_NEUTRED = 'N'
    PET_NO      = 'O'
    FIXED_CHOICES = [ (PET_SPAYED, 'Spayed'), (PET_NEUTRED, 'Neutred'), (PET_NO, 'No')]

    MERLE = 'M'; BRINDLE = 'B'; SPOTTED = 'S'; BLUE = 'BL'; BLACK='BK'; SILVER = 'SL'; WHITE = 'W'; CREAM = 'CR'; FAWN = 'F'; 
    LIGHTBROWN='L'; DARKBROWN = 'D'; RED = 'R'; GREYTABBY = 'GT'; REDTABBY = 'RT'; TUXEDO = 'T'; TORTISESHELL = 'TT'; CALICO = 'C'
    YELLOW = 'Y'; AMBER = 'A'; GREY = 'G'; GREEN = 'GR'
    BODY_COLOR = [ 
        (MERLE, 'merle'), (BRINDLE, 'brindle'), (SPOTTED, 'spotted'), (BLUE, 'blue'), (BLACK, 'black'), (SILVER, 'silver'),
        (WHITE, 'white'), (CREAM, 'cream'), (FAWN, 'faWN'), (LIGHTBROWN, 'lightbrown'), (DARKBROWN, 'darkbrown'), (RED, 'red'),
        (GREYTABBY, 'greytabby'), (REDTABBY, 'redtabby'), (TUXEDO, 'tuxedo'), (TORTISESHELL, 'tortiseshell'), (CALICO, 'calico'),
        
        ]

    EYE_COLOR = [ 
        (YELLOW, 'yellow'), (AMBER, 'amber'), (GREY, 'grey'), (GREEN, 'Green'), 
        (BLUE, 'blue'), (LIGHTBROWN, 'lightbrown'), (DARKBROWN, 'darkbrown')
    ]

    PET_LOST = 'L'
    PET_FOUND = 'F'
    PET_DF = 'D'
    PET_CHOICES = [ (PET_LOST, 'Lost'), (PET_FOUND, 'Found'), (PET_DF, '---Select Type---')]

    
    #PET_TYPE = forms.ChoiceField(choices=PET_CHOICES, widget=forms.RadioSelect)
    
    pet_type    = models.CharField(max_length=25,  blank=True)
    species     = models.CharField(max_length=255, blank=True)
    body_color  = models.CharField(max_length=30,  blank=True)
    eye_color   = models.CharField(max_length=30,  blank=True)
    description = models.CharField(max_length=255, blank=True)
    picture     = models.ImageField(null=True)
    gender      = models.CharField(max_length=25, blank=True)
    fixed       = models.CharField(max_length=25, blank=True)
    breed       = models.CharField(max_length=255, blank=True)
    employee    = models.ForeignKey(Employee, on_delete=models.PROTECT, blank=True, null=True )
    owner       = models.ForeignKey(PetOwner, on_delete=models.PROTECT,  blank=True, null=True )
    date_reported = models.DateField(default=timezone.now, blank=True)
    date_lost    = models.DateField(null=True, blank=True)
    date_found   = models.DateField(null=True, blank=True)
    street       = models.CharField(max_length=255, blank=True)
    city         = models.CharField(max_length=255, blank=True, default='Orlando')
    zip_code     = models.CharField(max_length=15, blank=True, default=32819)
    state        = models.CharField(max_length=30, default="Florida")

    def __str__(self):
        return self.species 