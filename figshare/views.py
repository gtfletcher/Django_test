from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .methods import *

import requests 
#from oauth_hook import OAuthHook
from requests_oauthlib import OAuth1
from MSfigshare.settings.base import DEBUG

from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse

if DEBUG:
    from MSfigshare.settings.local import CLIENT_ID, CLIENT_SECERT # Figshare API access
else:
    from MSfigshare.settings.production import CLIENT_ID, CLIENT_SECERT  # Figshare API access

import json

from .forms import FigShareForm , FigShare_AuthorForm , FigShare_Resource_Form

#def resource_author (request):

#    context = {}

class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')



@login_required()
def secret_page(request, *args, **kwargs):
    return HttpResponse('Secret contents!', status=200) # no render view

@login_required()
def gen_search(request):
    title = "Figshare Search"
    form = FigShareForm(request.POST or None) # call constructor 
    context = {
        "form" : form ,
        "title": title, 
    }


    # post request after valid input
    if form.is_valid():
        instance = form.save(commit=False) # but do not save to db
        
                
        
        # set form locals         
        author_name = form.cleaned_data.get("author_name") # get the cleaned data after all our validation
        resource_name = form.cleaned_data.get("resource_name")
        resource_doi = form.cleaned_data.get("resource_doi")
        resource_link = form.cleaned_data.get("resource_link")
        resource_id = form.cleaned_data.get("resource_id")
       
        for key , val in form.cleaned_data.iteritems():
           
           print key,' is = ' , val
       
        client = requests.session()
        
        token_key = 'z3UtX8IK2INOctmOKu8KpAnERq3z5HWyUEXmBeQKLYYgz3UtX8IK2INOctmOKu8KpA'
        token_secret = 'O1KaANDRn0FKiaq5BjIviw'
        oauth = OAuth1(client_key=CLIENT_ID, client_secret=CLIENT_SECERT,
               resource_owner_key=token_key, resource_owner_secret=token_secret,
               signature_type = 'auth_header')        
                
        
        #body = {'title':'Test dataset', 'description':'Test description','defined_type':'dataset'}
        #headers = {'content-type':'application/json'}

        

        #response = client.post('http://api.figshare.com/v1/my_data/articles', auth=oauth,
        #                data=json.dumps(body), headers=headers)
        results = AuthorSearch(author_name , client , oauth)
        
        print results
        print
        
        if resource_id and resource_link:
            # add link to figshare article id            
            results = Addlink( resource_id ,  resource_link,  client , oauth )                        
                        
            results = ArticleDetails(resource_id , client , oauth)
            print results
            print
        

    return render(request, "figshare/FigShareAPI_Auth_search.html" , context ) # basic get request



@login_required()
def Author_Search(request):
    title = "Figshare Author Search"
    form = FigShare_AuthorForm(request.POST or None) # call constructor 
    context = {
        "form" : form ,
        "title": title, 
    }
    # post request after valid form input (Ask figshare api about the author)
    if form.is_valid():
        instance = form.save(commit=False) # but do not save to db
        # set form locals         
        author_name = form.cleaned_data.get("author_name") # get the cleaned data after all our validation
        for key , val in form.cleaned_data.iteritems():           
           print key,' is = ' , val
        
        #Getting info from figshare 
        client = requests.session()        
        # oauth1 token keys and setup 
        TOKEN_KEY = 'z3UtX8IK2INOctmOKu8KpAnERq3z5HWyUEXmBeQKLYYgz3UtX8IK2INOctmOKu8KpA'
        TOKEN_SECERT = 'O1KaANDRn0FKiaq5BjIviw'                          
        oauth = OauthSetup( CLIENT_ID , CLIENT_SECERT , TOKEN_KEY , TOKEN_SECERT)                        
        #API AuthorSearch method        
        results = AuthorSearch(author_name , client , oauth)
        
        print results
        print
        #Add results to Quary set 
        QuerySet = results.get("items")
        if len(QuerySet) == 0 :
            QuerySet.append({'full_name':'No Users Found'})            
            
        print "QuarySet is = ", QuerySet        
        context = {
        "form" : form ,
        "title": title, 
        "queryset" : QuerySet,        
        }        
        
    return render(request, "figshare/FigShareAPI_Auth_search.html" , context ) # basic get request

@login_required()
def Article_Search(request):
    title = "Figshare Article Search" 
    form = FigShare_Resource_Form(request.POST or None) # call constructor 
    context = {
        "form" : form ,
        "title": title, 
    }
    # post request after valid form input (Ask figshare api about the author)
    if form.is_valid():
        instance = form.save(commit=False) # but do not save to db
        # set form locals         
        article_id = form.cleaned_data.get("resource_id") # get the cleaned data after all our validation
        for key , val in form.cleaned_data.iteritems():           
           print key,' is = ' , val
        
        #Getting info from figshare 
        client = requests.session()        
        # oauth1 token keys and setup 
        TOKEN_KEY = 'z3UtX8IK2INOctmOKu8KpAnERq3z5HWyUEXmBeQKLYYgz3UtX8IK2INOctmOKu8KpA'
        TOKEN_SECERT = 'O1KaANDRn0FKiaq5BjIviw'                          
        oauth = OauthSetup( CLIENT_ID , CLIENT_SECERT , TOKEN_KEY , TOKEN_SECERT)                        
        #API AuthorSearch method        
        results = ArticleDetails(article_id , client , oauth)
        
        print results
        print
        #Add results to Quary set 
        QuerySet = results.get("items")
        if len(QuerySet) == 0 :
            QuerySet.append({'full_name':'No Article Found'})            
            
        print "QuarySet is = ", QuerySet        
        #Add QuerySet to context so we can render it in the html page
        context = {
        "form" : form ,
        "title": title, 
        "queryset" : QuerySet,        
        }        
        
    return render(request, "figshare/FigShareAPI_Art_search.html" , context ) # basic get request


