import sys, os
import time
from django.db import models
from django.urls.base import reverse

# class Category(models.Model):
#     name = models.CharField(max_length=255, null=True, db_index=True, blank=True)

#     def __str__(self):
#         return self.name

class Myfeed(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, default='')
    slug = models.SlugField(null=True, blank=True, max_length=255)
    description = models.TextField(max_length=255,db_index=True, blank=True, null=True)
    # category = models.ForeignKey(Category, blank=True, null=True, default='', related_name='category')
    category = models.CharField(max_length=255, null=True, db_index=True, blank=True)
    tag_id = models.CharField(max_length=255, blank=True, null=True, db_index=True, default='')

    main_link = models.URLField(db_index=True, default='')
    sub_link = models.URLField(db_index=True, default='')
    published = models.CharField(max_length=255, blank=True, db_index=True, default='')
    updated = models.CharField(max_length=255, blank=True,null=True, db_index=True, default='')
    timestamp = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('myfeed',
                       kwargs={'slug': self.slug})
    def __unicode__(self):
        return self.title