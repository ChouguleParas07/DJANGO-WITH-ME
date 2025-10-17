from django.urls import path
from . import views

urlpatterns =[
    path('<int:pk>/', views.emp_detail, name='emp_details'),

]