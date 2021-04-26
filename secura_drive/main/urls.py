from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='index'),
    path('drive/', drive_page),
    path('delete/<str:id>', delete_file),
    path('view/<str:id>', view_file),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
]
