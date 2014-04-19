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

from django.db import models

# Create your models here.

from djangotoolbox.fields import ListField
from djangotoolbox.fields import EmbeddedModelField


class Post(models.Model):
    body = models.TextField()
    permalink = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    tags = ListField()
    comments = ListField(EmbeddedModelField('Comment'))
    date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    body = models.TextField()
    email = models.EmailField()
    author = models.CharField(max_length=255)
