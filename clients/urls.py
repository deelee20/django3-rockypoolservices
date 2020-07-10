from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [
    
   path('', views.new_client, name = 'clients'),
   path('repair_request', views.repair, name = 'repair'),
]