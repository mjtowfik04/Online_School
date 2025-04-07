from django.contrib import admin
from courses.models import Course, Category, Review
# Register your models here.
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Review)