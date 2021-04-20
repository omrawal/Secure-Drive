from django.urls import path
from .views import *
urlpatterns = [
    path('file', FileAPIView.as_view()),
    path('file/<str:fid>', FileOperations.as_view()),
    # path('file/', FiletList.as_view()),
    # path('file/<str:fid>', FileDetail.as_view()),
]
