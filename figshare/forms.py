from django import forms
from .models import FigShare , PubSearch 

class FigShareForm(forms.ModelForm):
    class Meta:
        model = FigShare
        fields = [         # resource fields in form we want
        'author_name',
        'resource_name',
        'resource_doi',
        'resource_link',
        'resource_id',
        ]

    # our defined cleaning of data
    def clean_author_name (self):
        author_name = self.cleaned_data.get('author_name')
        # add validation code
        return author_name

        
    def clean_resource_name (self):
        resource_name = self.cleaned_data.get('resource_name')
        # add validation code
        return resource_name


    def clean_resource_doi (self):
        resource_doi = self.cleaned_data.get('resource_doi')
        # add validation code
        return resource_doi

    def clean_resource_link (self):
        resource_link = self.cleaned_data.get('resource_link')
        # add validation code
        return resource_link

    def clean_resource_id (self):
        resource_id = self.cleaned_data.get('resource_id')
        # add validation code
        return resource_id
                        
# Author Search form (just need the author name)    
class FigShare_AuthorForm(forms.ModelForm):
    class Meta:
        model = FigShare
        fields = [         # fields in form we want
        'author_name',
        ]

    # our defined cleaning of data
    def clean_author_name (self):
        author_name = self.cleaned_data.get('author_name')
        # add validation code
        return author_name


class FigShare_Resource_Form(forms.ModelForm):
    class Meta:
        model = FigShare
        fields = [         # resource fields in form we want
        'resource_id',   
        ]

    # our defined cleaning of data
    def clean_resource_id (self):
        resource_id = self.cleaned_data.get('resource_id')
        # add validation code
        return resource_id

#Public search form
class PubSearchForm(forms.ModelForm):
    class Meta:
        model = PubSearch
        fields = [
        'search_for',  # Public Search form
        'date_from' ,  # search for articles since
        'date_to'   ,  # articles to. Date format is: 2012-06-12 (YYYY-MM-DD)
        'has_author',  # Article has author of
        'has_title' ,  # Article has title of
        'has_category',  # Article has cat. of
        'has_tag'    , # Article has tag of           
        'page'       , # page number of results 
        ]
        
        # our defined cleaning of data
    def clean_search_for (self):
        search_for = self.cleaned_data.get('search_for')
        # add extra validation code for field
        return search_for
        
    def clean_date_from (self):
        date_from = self.cleaned_data.get('date_from')
        return date_from
        
    def clean_date_to (self):
        date_to = self.cleaned_data.get('date_to')
        return date_to
        
    def clean_has_author (self):
        has_author= self.cleaned_data.get('has_author')
        return has_author
        
    def clean_has_title (self):
        has_title = self.cleaned_data.get('has_title')
        return has_title
        
    def clean_has_category (self):
        has_category = self.cleaned_data.get('has_category')
        return has_category
        
    def clean_has_tag (self):
        has_tag = self.cleaned_data.get('has_tag')
        return has_tag
    
    def clean_page (self):
        page = self.cleaned_data.get('page')
        return page
    