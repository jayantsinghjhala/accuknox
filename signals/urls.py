from django.urls import path
from signals import views

urlpatterns = [
    path('create_user/', views.create_user_view, name='create_user'),
    path('rectangle/', views.rectangle_view, name='rectangle'),
]
