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

# add links via json data     
def Addlink_json( article_id ,  jsondata ,  client , oauth ):
    # headers to send to api need json to decode the body
    headers = {'content-type':'application/json'}
    # these do not change    
    put_command = 'http://api.figshare.com/v1/my_data/articles/' + str(article_id) + '/links'

    # link is a dict with key=link    jsondata.links is an array of link dicts
    for link in jsondata.get("links"):
        # content body to send to api    
        body = { }
        # add link to body
        body['link'] = link.get("link")
        response = client.put(put_command, auth=oauth,
                        data=json.dumps(body), headers=headers)    

        result = json.loads(response.content)
        print result
    
    return ArticleDetails(article_id, client, oauth) # return the updated articledetails

#add tags via json
def Addtag_json( article_id ,  jsondata ,  client , oauth ):
    # headers to send to api need json to decode the body
    headers = {'content-type':'application/json'}
    # these do not change    
    put_command = 'http://api.figshare.com/v1/my_data/articles/' + str(article_id) + '/tags'

    # link is a dict with key=link    jsondata.links is an array of link dicts
    for tag in jsondata.get("tags"):
        # content body to send to api    
        body = { }
        # add link to body
        body['tag_name'] = tag.get("tag_name")
        response = client.put(put_command, auth=oauth,
                        data=json.dumps(body), headers=headers)    

        result = json.loads(response.content)
        print result
    
    return ArticleDetails(article_id, client, oauth) # return the updated articledetails

#add files from json information
def Addfiles_json(article_id, jsondata ,client, oauth  ):
    
    put_command = 'http://api.figshare.com/v1/my_data/articles/'+str(article_id)+'/files'
    for article_file in jsondata.get("files"): 
        print "##### debug ######"        
        print article_file 
        fpath = article_file.get("filepath")
        namelist = fpath.split('/')
        name = namelist[-1]
        print name
        files = {'filedata':(name, open(fpath, 'rb'))}
        response = client.put(put_command, auth=oauth,
                      files=files)
        results = json.loads(response.content)
        print results        
        
    return ArticleDetails(article_id, client, oauth) # want to want article details
    
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

# gets the url/doi of a public search result (made with PublicSearch)
#           public result dict  session
def GetArticleResults(item , client):
    APIurl = item.get('url')  # This is the api article get request  
    response = client.get(APIurl)
    link_result = json.loads(response.content)
    # Add the article results we want to pass to QuerySet for rendering on html page
    results = {}    
    results["figshare_url"] = link_result.get("items")[0].get("figshare_url") # get figshare url
    results["publisher_doi"] =link_result.get("items")[0].get("publisher_doi") # get doi publisher 
    #print results          
    return results 
    # returns a dict of results to update the queryset dict

# creates figshare article from json template
#               json dict   session   oauth1
def CreateArticle(jsondata, client , oauth):
    
    #body = {'title':'Test dataset', 'description':'Test description','defined_type':'dataset'} required
    body = {}
    body["title"]=jsondata.get("title")
    body["description"]=jsondata.get("description")
    body["defined_type"]=jsondata.get("defined_type")
        
    print body   
    print      
    headers = {'content-type':'application/json'}   
    
    post_command = 'http://api.figshare.com/v1/my_data/articles' 
    
    response = client.post(post_command,auth=oauth , data=json.dumps(body) , headers=headers )    
    results = json.loads(response.content)    
    
    return results # returns the api response which contains article_info including ID

# delete private/draft article via article_id
#                article id    session   oauth1
def DeleteArticle(article_id , client , oauth ):

    delete_command = 'http://api.figshare.com/v1/my_data/articles/' + str(article_id)
    response = client.delete(delete_command, auth=oauth)
    results = json.loads(response.content)
    return results

# make draft/private article public
#             article_id     session  oauth1 
def MakePublic(article_id , client , oauth ):

    public_command = 'http://api.figshare.com/v1/my_data/articles/'+ str(article_id)+'/action/make_public'
    response = client.post(public_command , auth=oauth)
    results = json.loads(response.content)
    return results

# make draft private article
#             article_id     session  oauth1 
def MakePrivate(article_id , client , oauth ):

    private_command = 'http://api.figshare.com/v1/my_data/articles/'+ str(article_id)+'/action/make_private'
    response = client.post(private_command , auth=oauth)
    results = json.loads(response.content)
    return results
