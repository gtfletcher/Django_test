from django.shortcuts import render

from .forms import ContactForm, SignUpForm


# Create your views here.
def home(request):
    title=""
    if request.user.is_authenticated(): # is user logged in
        title = "Welcome back %s" %(request.user)
    else:
        title = "Welcome New user"

    if request.method == "POST":
        print request.POST

    # request.POST is the raw data never use request.POST['email']
    form = SignUpForm(request.POST or None) # call constructor (the request gets called when we want to submit something as well
    context = {
        "template_title" : title,
        "form" : form , 
    }


    # If data makes it through our validation we can edit it or set default
    if form.is_valid():
        instance = form.save(commit=False) # but do not save to db
        local_full_name = form.cleaned_data.get("full_name") # get the cleaned data after all our validation
        if not instance.full_name:
            instance.full_name = "Unknown"
        print instance 
        instance.save()
        context = { "template_title" : "Thank you for Signing up"}

         
    return render(request, "home.html" , context )


def contact(request):
    title = "Contact"
    form = ContactForm(request.POST or None) # call constructor (the request gets called when we want to submit something as well
    context = {
    "form" : form ,
    "title": title,
    }

    if form.is_valid():
        for key , val in form.cleaned_data.iteritems():

            if key == "full_name" and not val:
                print "key is full_name and no name"
                form.full_name = val ="Unknown"
#                val = form.cleaned_data.get(key)
                print "value of field is now:" , val
                
            print key , val

            
    return render(request, "contact.html" , context )

