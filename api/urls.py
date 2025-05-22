from django.urls import path, include
from courses.views import CategoryViewSet, CourseViewSet, ReviewViewSet, CourseImageViewSet, CategoryImageViewSet
from order.views import EnrollCreateView,initiate_payment
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('course', CourseViewSet)
router.register('categories', CategoryViewSet)

# Remove this line:
# router.register('enroll', EnrollCreateView, basename='enroll')

course_router = routers.NestedSimpleRouter(router, 'course', lookup='course')
course_router.register('images', CourseImageViewSet, basename='course-images')
course_router.register('cimages', CategoryImageViewSet, basename='Category-images')
course_router.register('reviews', ReviewViewSet, basename='course-review')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(course_router.urls)),
    path('enroll/', EnrollCreateView.as_view(), name='enroll-create'),  # ✅ added correctly
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('payment/initiate/',initiate_payment,name="initiate_payment"),
    path("payment/success/", payment_success, name="payment-success"),
    path("payment/fail/", payment_fail, name="payment-fail"),
    path("payment/cancel/", payment_cancel, name="payment-cancel"),
]

