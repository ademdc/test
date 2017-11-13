from django.shortcuts import render
from django.conf.urls import url,include
from . import views
from todolist.views import *

urlpatterns = [
    url(r'^$', views.index, name='index'), 
    url(r'^todos/$', views.todos, name='todos'), 
    url(r'^todo/(?P<id>\w{0,50})/$', views.todo_individual,name='todo'), 
    url(r'^add/$', views.add, name='add'), 
    url(r'^contact/$', views.contact, name='contact'), 
    url(r'^contacts/$', ContactView.as_view(template_name="about.html")),
    url(r'^register/$', UserRegisterView.as_view(),name=''),
    url(r'^profile/$', UserProfileView.as_view(),name='profile'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^login/$', UserLoginView.as_view(), name=''), 

    #url(r'^login/$', main_page),
    #url(r'^user/(\w+)/$', user_page),
    #url(r'^login/$', 'django.contrib.auth.views.login')


]