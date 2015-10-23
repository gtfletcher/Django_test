from django.db import models

# Create your models here.
# Standard private searches and create Article model
class FigShare(models.Model):
    resource_name = models.CharField(max_length=80,blank=False)  # Name of the resource
    author_name = models.CharField(max_length=80,blank=False)  # Name of the author of the article
    resource_doi = models.URLField(default="",blank=False)  # Article doi
    resource_link = models.URLField(default="",blank=False)  # Article link 
    resource_id = models.IntegerField(default=0, blank=False) # Article Unique ID
   

    def __unicode__(self): # __str__ python 3
        return self.resource_name # must be a str()
        
        
#Public search api form 
class PubSearch(models.Model):
    search_for = models.CharField(max_length=80, blank=False, default="", verbose_name="Search Query" ,help_text="Please enter key phrase") # Public Search form
    date_from = models.DateField(blank=True, verbose_name="Search From" ,help_text="Date format is: 2015-12-25 (YYYY-MM-DD)")  # search for articles since
    date_to = models.DateField(blank=True, verbose_name="Search to" ,help_text="Date format is: 2015-12-25 (YYYY-MM-DD)")  # Date format is: 2012-06-12 (YYYY-MM-DD)
    has_author = models.CharField(max_length=80, blank=True, default="", verbose_name="Author") # Article has author of
    has_title = models.CharField(max_length=80, blank=True, default="", verbose_name="Title") # Article has title of
    has_category = models.CharField(max_length=80, blank=True, default="",verbose_name="Category") # Article has cat. of
    has_tag = models.CharField(max_length=80, blank=True, default="", verbose_name="Tag") # Article has tag of
    page = models.IntegerField(default=1, blank=False, verbose_name="Results Page Number") # which page of results do we want
    def __unicode(self):
        return self.search_for
