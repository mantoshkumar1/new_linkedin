from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('', views.AccountView.as_view(), name='account'),
]