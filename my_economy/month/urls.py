from django.urls import path
from . import views

urlpatterns = [
    path('', views.month_list, name='months'),
    path('<str:month>/<int:year>/', views.month_detail, name='month')
]