from django.db import models
from django.utils.text import slugify
from django.urls import reverse

from django.db import models
import datetime as dt

class Comments(models.Model):
    title = models.CharField(max_length=255, default="")
    entry = models.TextField(default = "")
    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=255, default='')
    def __str__(self):
        return self.title

class Tag(models.Model): # < here
    title = models.CharField(max_length=255, default='')
    slug = models.SlugField(blank=True, default='') # < here
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs): # < here
        self.slug = slugify(self.title)
        super(Tag, self).save()
    def get_absolute_url(self): # < here
        return reverse('tags', args=[str(self.slug)])


        
class Flower(models.Model):
    title = models.CharField(max_length=255, default= "")
    description = models.TextField(default='')
    slug = models.SlugField(blank=True, default='')
    category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)
    added = models.DateTimeField(default= dt.datetime.now())
    comments = models.ManyToManyField(Comments)
    
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Flower, self).save()
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.slug)])

