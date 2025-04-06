from django.urls import path ,include
from courses.views import  CategoryViewSet,CourseViewSet,ReviewViewSet
from rest_framework_nested import routers

router= routers.DefaultRouter()
router.register('course',CourseViewSet)
router.register('categories', CategoryViewSet)

course_router= routers.NestedSimpleRouter(router,'course',lookup='course')
course_router.register('reviews',ReviewViewSet,basename='course-review')


urlpatterns = [
    path('',include(router.urls)),
    path('',include(course_router.urls))
]