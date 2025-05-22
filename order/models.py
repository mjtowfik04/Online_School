
from django.db import models
from django.conf import settings
from courses.models import Course

class Enroll(models.Model):
    Email= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{ self.Email} enrolled in {self.course.title}"
