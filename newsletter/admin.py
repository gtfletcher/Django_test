from django.contrib import admin

# Register your models here.

#Import our custom forms from forms.py
from .forms import SignUpForm

# import our custom database models from models.py
from .models import SignUp

# this uses the admin form 
class SignUpAdmin(admin.ModelAdmin):
#             what we return in SignUp   Names of extra fields in SignUp we want to display 
    list_display = ["__unicode__" , "timestamp" , "updated"]
    form = SignUpForm
    #    class Meta:
    #        model = SignUp

admin.site.register(SignUp , SignUpAdmin)
