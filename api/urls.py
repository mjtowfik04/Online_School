from django.urls import path ,include
from courses.views import  CategoryViewSet,CourseViewSet,ReviewViewSet,CourseImageViewSet,CategoryImageViewSet
from order.views import CartViewSet, CartItemViewSet, OrderViewset

from rest_framework_nested import routers

router= routers.DefaultRouter()
router.register('course',CourseViewSet)
router.register('categories', CategoryViewSet)
router.register('carts', CartViewSet, basename='carts')
router.register('orders', OrderViewset, basename='orders')

course_router= routers.NestedSimpleRouter(router,'course',lookup='course')
course_router.register('images', CourseImageViewSet,basename='course-images')
course_router.register('cimages',CategoryImageViewSet,basename='Category-images')
course_router.register('reviews',ReviewViewSet,basename='course-review')
cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items', CartItemViewSet, basename='cart-item')




urlpatterns = [
    path('',include(router.urls)),
    path('',include(course_router.urls)),
    path('', include(cart_router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]