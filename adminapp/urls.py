from django.urls import path

import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
path('products/create/', adminapp.ProductCreateView.as_view(), name='product_create'),
    path('products/read/', adminapp.ProductListView.as_view(), name='products'),
    path('products/read/category/<int:category_pk>/', adminapp.ProductListView.as_view(), name='products_by_category'),
    path('products/read/<int:pk>/', adminapp.ProductDetailView.as_view(), name='product_read'),
    path('products/update/<int:pk>/', adminapp.ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', adminapp.ProductDeleteView.as_view(), name='product_delete'),
]