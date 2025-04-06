from django.urls import path
from curses import views

urlpatterns = [
    path('', views.CoursList.as_view(), name='product-list'),
    path('<int:id>/', views.CoursDetails.as_view(), name='product-list'),
]