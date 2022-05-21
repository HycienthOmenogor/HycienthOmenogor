from django.urls import path
from . import views

urlpatterns = [
        path('', views.SoldListView.as_view(), name='sold-list'),
        path('sale/<int:pk>/', views.SoldDetailView.as_view(), name='sold-detail'),
]
