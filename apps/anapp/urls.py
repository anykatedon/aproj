from django.urls import path
from . import views

app_name='feedback'

urlpatterns = [
    path('', views.feedback_form, name='home'),
    path('doctor/', views.search_doctor, name='search_doctor'),
    path('ajax/validate_doctorname/', views.validate_doctorname, name='validate_doctorname'),
]
