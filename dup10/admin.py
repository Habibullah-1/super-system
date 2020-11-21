from django.contrib import admin

from django.contrib import admin
from .models import Flower, Category, Tag, Comments
admin.site.register(Flower)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comments)