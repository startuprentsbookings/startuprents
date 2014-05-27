# Copyright 2014 Rents and Bookings
#
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from django.conf.urls import patterns, url

#Django Tutorial
#from apparmor.easyprof import valid_template_name
from rentsapp import views

#Django-MongoDB-Engine tutorial
from django.views.generic import ListView, DetailView
from models import Post



#Django Tutorial
urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)


#Django-MongoDB-Engine tutorial
post_detail = DetailView.as_view(model=Post, template_name='post_detail.tpl')
post_list = ListView.as_view(model=Post, template_name='post_list.tpl')

urlpatterns = patterns('',
    url(r'^post/(?P<pk>[a-z\d]+)/$', post_detail, name='post_detail'),
    url(r'^$', post_list, name='post_list'),
)

