from django.urls import path
from .views import *
urlpatterns = [
    path('', home),
    path('drive/', drive_page),
    path('delete/<str:id>',delete_file),
    path('view/<str:id>',view_file)
]
