from django import forms

from .models import FigShare

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