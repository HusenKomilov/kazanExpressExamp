from django.urls import path
from examp import views

urlpatterns = [
    path('shop/', views.ShopListCreateAPIView.as_view()),
    path('shop/<int:pk>/update/', views.ShopRetrieveUpdateAPIView.as_view()),
    path('shop/<int:pk>/delete/', views.ShopDeleteAPIView.as_view()),

    path('category/', views.CategoryListCreateAPIView.as_view()),
    path('category/<int:pk>/update/', views.CategoryRetrieveUpdateAPIView.as_view()),
    path('category/<int:pk>/delete/', views.CategoryDeleteAPIView.as_view()),

    path('product/', views.ProductListAPIView.as_view()),
    path('product/create/', views.ProductCreateAPIView.as_view()),
    path('product/<int:pk>/update/', views.ProductRetrieveUpdateAPIView.as_view()),
    path('product/<int:pk>/delete/', views.ProductDeleteAPIView.as_view()),
]

