
from django.db import models
from django.conf import settings
from courses.models import Course

class Enroll(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course') 

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} enrolled in {self.course.title}"
