
from django.contrib import admin
from django.urls import path, include
from dup10 import views as myapp_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp_views.index, name='index'),
    path('accounts/', include('allauth.urls')),
    path('flower/<slug:slug>/', myapp_views.detail, name='detail'),
    path('', myapp_views.index, name='index'),
    path('tags/<slug:slug>/', myapp_views.tags, name='tags'),
    path('flower/edit/<int:pk>/', myapp_views.edit, name='edit'),
    path('flowe/create/', myapp_views.create, name='create'),     path('flower/delete/<int:pk>/', myapp_views.delete, name='delete'),
]
