from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse

import json

from .forms import FigShareForm

#def resource_author (request):

#    context = {}

class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')



@login_required()
def secret_page(request, *args, **kwargs):
    return HttpResponse('Secret contents!', status=200)

#    
#    return render(request, "home.html" , context )
# Create your views here.
#
