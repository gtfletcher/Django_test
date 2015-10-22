"""MSfigshare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static 
from django.contrib import admin

from figshare.views import ApiEndpoint  # our api input class with the oauth2 get request

# list of URL patterns
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)), # admin page
    url(r'^contact/$' , 'newsletter.views.contact' , name='contact' ), # contact page
    url(r'^aboutus/$' , 'MSfigshare.views.about' , name='aboutus' ), # aboutus page
    url(r'^$' , 'newsletter.views.home' , name='home' ), # all other pages
    url(r'^accounts/', include('registration.backends.default.urls')), # accounts/register accounts/login
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')), # oauth2 toolkit for figshare
    url(r'^api/hello', ApiEndpoint.as_view()),  # figshare api and also resource server!
    url(r'^api/secret$', 'figshare.views.secret_page', name='secret'), # test login only api page
    url(r'^figshare/search$' ,'figshare.views.Author_Search', name='gen_search'  ), # general search form
    url(r'^figshare/author$' ,'figshare.views.Author_Search', name='auth_search'  ), # general search form
    url(r'^figshare/article$' ,'figshare.views.Article_Search', name='art_search'  ), # general search form
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
