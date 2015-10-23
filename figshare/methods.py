# -*- coding: utf-8 -*-
import requests 
#from oauth_hook import OAuthHook
from requests_oauthlib import OAuth1
import json

# setup oauth for other methods # needs oauth2 3 legged auth for other peoples resources
#            API_app id     API_app sec  , resource token   resource sec 
def OauthSetup( CLIENT_ID , CLIENT_SECERT , TOKEN_KEY , TOKEN_SECERT):
    

    oauth = OAuth1(client_key=CLIENT_ID, client_secret=CLIENT_SECERT,
               resource_owner_key=TOKEN_KEY, resource_owner_secret=TOKEN_SECERT,
               signature_type = 'auth_header')              
    return oauth

#   Search figshare for author
#             Author from form  session  oauth header
def AuthorSearch(author_name, client ,oauth):
    
    search_command = 'http://api.figshare.com/v1/my_data/authors?search_for='+ author_name
    response = client.get(search_command , auth=oauth)

    #response = client.post('http://api.figshare.com/v1/my_data/articles', auth=oauth,
    #                data=json.dumps(body), headers=headers)
    results = json.loads(response.content)
    return results

# Get details of an article by its ID
                #article_id     session  oauth header
def ArticleDetails(article_id , client , oauth):

    search_command='http://api.figshare.com/v1/my_data/articles/'+ str(article_id)   
    response = client.get(search_command , auth=oauth)
    results = json.loads(response.content)
    return results
    
# Adds resource link to article using id
#            id          html_link   session  oauth header 
def Addlink( article_id ,  link ,  client , oauth ):

    # content body to send to api    
    body = { }
    # add link to body
    body['link'] = link
    # headers to send to api need json to decode the body
    headers = {'content-type':'application/json'}
    put_command = 'http://api.figshare.com/v1/my_data/articles/' + str(article_id) + '/links'
    response = client.put(put_command, auth=oauth,
                        data=json.dumps(body), headers=headers)    

    results = json.loads(response.content)
    return results
    
#Public FigShare API search
#             body dict  session  oauth  
def PublicSearch (body , client ):
    headers = {'content-type':'application/json'}
    search_command= 'http://api.figshare.com/v1/articles/search?search_for='+body.get('search_for')
    for key, val in body.iteritems():
        if not key == 'search_for': 
            search_command += '&'+ key + '=' + str(val)
    
    #print search_command
    response = client.get(search_command)
    results = json.loads(response.content)
    return results

# public search for an article
def PubArtSearch ( article_id , client ):    
    search_command = 'http://api.figshare.com/v1/articles/'+ str(article_id)
    response = client.get(search_command)
    results = json.loads(response.content)
    return results

# gets the url of a public search result (made with PublicSearch)
def GetArticleURL(item , client):
    APIurl = item.get('url')  # This is the api article get request  
    response = client.get(APIurl)
    link_result = json.loads(response.content)
    url = link_result.get("items")[0].get("figshare_url")
    #print "Article url is =" , url            
    return url

