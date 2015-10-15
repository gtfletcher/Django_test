from django.db import models

# Create your models here.
class FigShare(models.Model):
    resource_name = models.CharField(max_length=80,blank=False)
    author_name = models.CharField(max_length=80,blank=False)
    resource_doi = models.URLField()
    resource_link = models.URLField()

    def __unicode__(self): # __str__ python 3
        return self.resource_name # must be a str()
