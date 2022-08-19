from django.urls import path
from . import views
from .models import Sold

urlpatterns = [
        path('', views.SoldIndexView.as_view(),
            name='sold-dates-list'),

        path('products/', views.ProductsListView.as_view(),
            name='products-list'),

        path('products/create/',
            views.ProductEntryView.as_view(),
            name='products-create'),

        path('products/delete/<int:pk>/',
            views.ProductsDeleteView.as_view(),
            name='products-delete'),

        path('products/update/<int:pk>/',
            views.ProductsUpdateView.as_view(),
            name='products-update'),

        path('products/<slug:product_detail>/', views.ProductsDetailView.as_view(),
            name='products-detail'),

        path('sale/<int:year>/<str:month>/<int:day>/',
            views.SoldDayArchiveView.as_view(),
            name='sold-archive'),

        # for <int:month> use (month_format='%m') inside .as_view function
        path('sale/<int:year>/<str:month>/<int:day>/<int:pk>/', 
            views.SoldDateDetailView.as_view(model=Sold, date_field='date'),
            name='sold-date-detail'),

        path('sale/create/', 
            views.SoldEntryView.as_view(), 
            name='sold-create'),

        path('sale/update/<int:pk>/',
            views.SoldUpdateView.as_view(),
            name='sold-update'),

        path('sale/delete/<int:pk>/',
            views.SoldDeleteView.as_view(),
            name='sold-delete'),
]
