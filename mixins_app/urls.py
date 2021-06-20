from django.urls import path
from mixins_app import views

urlpatterns=[
    path('employees/', views.EmployeeListView.as_view()),
    path('employees/<int:pk>/' , views.EmployeeDetailsView.as_view()),
]