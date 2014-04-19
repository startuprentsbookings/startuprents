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

from django.contrib import admin
from rentsapp.models import Post
from rentsapp.models import Comment


#class PostAdmin(admin.ModelAdmin):
#    fields = ('body', 'permalink', 'author', 'title', 'tags', 'comments', 'date')

#admin.site.register(Post, PostAdmin)
#TODO- Must be fix (Post) to be manage trough the admin page due to tags and comments
admin.site.register(Post)
admin.site.register(Comment)
