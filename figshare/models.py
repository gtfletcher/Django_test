from django.db import models

# Create your models here.
class FigShare(models.Model):
    resource_name = models.CharField(max_length=80,blank=False)  # Name of the resource
    author_name = models.CharField(max_length=80,blank=False)  # Name of the author of the article
    resource_doi = models.URLField(default="",blank=False)  # Article doi
    resource_link = models.URLField(default="",blank=False)  # Article link 
    resource_id = models.IntegerField(default=0, blank=False) # Article Unique ID

    def __unicode__(self): # __str__ python 3
        return self.resource_name # must be a str()