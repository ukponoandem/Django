
from django.urls import path
from . import views


    # path('about/', views.about, name='about'),
    # path('', views.welcome, name='welcome'),
urlpatterns = [
    path('Home/', views.Home, name='Home'),
    path('about/', views.about, name='about'),
    path('details/<int:id>/', views.details, name='details'),  # Updated URL pattern
    path('testing/',views.testing,name='testing')
]
