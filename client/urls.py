from django.urls import path 
from .import views
# from .views import ClientFormView
urlpatterns = [
    path('',views.clientsave,name='clientsave'),
    # path('e',views.edit_client,name='indexs'),
    # path('s', ClientFormView.as_view()),
]
