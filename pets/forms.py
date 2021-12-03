from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import PetOwner, Pet, Employee



class PetOwnerForm(ModelForm):
    class Meta:
        model = PetOwner
        fields = ('first_name', 'last_name', 'phone', 'email')

class PetForm(ModelForm):
    class Meta:
        model = Pet
        
        #pet_type = forms.ChoiceField( widget=forms.RadioSelect(), choices=Pet.PET_CHOICES)
        fields = ('date_reported', 'date_lost', 'date_found', 'pet_type','species', 'breed', 'gender', 'eye_color', 'body_color', 
                'fixed',  'picture', 'street', 'city', 'state', 'zip_code', 'description', 'employee' )


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'phone', 'email', 'username', 'password', 'type', 'street', 'city', 'zip_code', 'state')

    

        

        