from django.shortcuts import render
from django.conf.urls import url,include
from . import views
from comments.views import *

urlpatterns = [
    url(r'^$', CommentsView.as_view(), name='comments'), 
    url(r'^comments_form$', CommentsFormView.as_view(), name='comments_form'),
    url(r'^register/$', RegisterUserView.as_view(), name='register'),
    url(r'^login/$', LoginUserView.as_view(), name='login'),
    url(r'^profile/$', ProfileUserView.as_view(), name='profile'),
]