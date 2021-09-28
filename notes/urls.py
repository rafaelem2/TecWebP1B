from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('tag/<str:tag>' , views.tag, name = 'tag'),
    path('all_tags', views.all_tags, name = 'all_tags')
   
]