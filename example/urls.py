from django.urls import path

from .import views

urlpatterns = [
    path('',views.create,name='create'),
    path('meristaff/',views.index,name='example'),
    path('search/',views.search,name='search'),
    path('delete/<int:delete_id>/',views.delete,name='delete'),
    path('edit/<int:edit_id>/',views.edit,name='edit'),
]
