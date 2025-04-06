from django_filters.rest_framework import FilterSet
from courses.models import Course


class CoursetFilter(FilterSet):
    class Meta:
        model = Course
        fields = {
            'category_id': ['exact'],
            'price': ['gt', 'lt']
        }