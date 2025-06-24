from django.urls import path
from .views import Create_employee, update_employee, employee_list, delete_employee, deleted_history,search_employee




urlpatterns = [
    path('',employee_list,name='list'),
    path('Create/',Create_employee,name='create'),
    path('update/<int:pk>',update_employee,name='update'),
    path('delete/<int:pk>',delete_employee,name='delete'),
   path('deleted-history/', deleted_history, name='deleted_history'),
   path('search-employee/', search_employee, name='search_employee'), 


]
