from django.urls import path 
from .import views

urlpatterns = [
    path('',views.index,name='meristaff'),
    path('edit_client/<int:client_id>/',views.edit_clientdetails,name='edit_client'),
    path('edit_client_save/',views.edit_client_save,name='edit_client_save'),
    path('delete_client/<int:client_id>/',views.delete_client,name='delete_client')
]
