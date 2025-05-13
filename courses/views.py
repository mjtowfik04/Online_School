from courses.models import  Course, Category, Review,CourseImage,CategoryImage
from courses.serializers import CourseSerializer, CategorySerializer, ReviewSerializer,CourseImageSerializer,CategoryImageSerializer
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from courses.filters import CoursetFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from courses.paginations import DefaultPagination
from api.permissions import IsAdminOrReadOnly
from courses.permissions import IsReviewAuthorOrReadonly


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all().order_by('id')
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class =CoursetFilter
    pagination_class = DefaultPagination
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'updated_at']
    permission_classes = [IsAdminOrReadOnly]


class CourseImageViewSet(ModelViewSet):
    serializer_class = CourseImageSerializer
    permission_classes = [IsAdminOrReadOnly]


    def get_queryset(self):
        return CourseImage.objects.filter(course_id=self.kwargs.get('course_pk'))

    def perform_create(self, serializer):
        serializer.save(course_id=self.kwargs.get('course_pk'))


class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Category.objects.annotate(
        Course_count=Count('courses')).all()
    serializer_class = CategorySerializer

class CategoryImageViewSet(ModelViewSet):
    serializer_class =CategoryImageSerializer
    permission_classes = [IsAdminOrReadOnly]


    def get_queryset(self):
        return CategoryImage.objects.filter(category_id=self.kwargs.get('Category_pk'))

    def perform_create(self, serializer):
        serializer.save(category_id=self.kwargs.get('Category_pk'))


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadonly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Review.objects.filter(course_id=self.kwargs.get('course_pk'))

    def get_serializer_context(self):
        return {'course_id': self.kwargs.get('course_pk')}