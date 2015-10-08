from django.db import models

# Create your models here.
class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=80,blank=False,null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    likes_coffee = models.BooleanField(default=True)

    def __unicode__(self): # __str__ python 3
        return self.email # must be a str()
