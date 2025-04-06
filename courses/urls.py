from django.urls import path
from courses import views

urlpatterns = [
    path('', views.CourseViewSet, name='course-list'),
    # path('<int:id>/', views.ProductDetails.as_view(), name='product-list'),
]