#lists the web forms for the end user
from django import forms

from .models import SignUp

class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=60 , required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1200)

    #def clean_email(self): ......
    
class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name','email']
        #exclude = ['full_name']  # all but full_name  <-- not very useful

    # add validation methods
    def clean_email(self):
        email = self.cleaned_data.get('email') # gets the email from the 'cleaned' dict saved from the form
        #additional Validation

        #set two parts of the email
        email_base , email_host = email.split("@")
        email_extension = email_host.split('.')
        #        print email_extension
        if len(email_extension) > 2:
            if not email_extension[-1]=='uk' or not email_extension[-2] == 'ac':
                raise forms.ValidationError("Please use a valid UK Uni email address (.ac.uk)")
        else:
            raise forms.ValidationError("Please use a valid UK Uni email address domain (domain.ac.uk)")
            
        return email


    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        # add validation code
        return full_name