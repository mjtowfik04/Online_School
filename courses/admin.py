from django.contrib import admin
from courses.models import Course, Category, Review,CategoryImage
# Register your models here.
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(CategoryImage)
admin.site.register(Review)