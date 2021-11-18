from django.contrib import admin

from .models import Pet, PetOwner, Employee, State, Breed, Species

admin.site.register(Pet)
admin.site.register(PetOwner)
admin.site.register(Employee)
admin.site.register(State)
admin.site.register(Breed)
#admin.site.register(Color)
admin.site.register(Species)
