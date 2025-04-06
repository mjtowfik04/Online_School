from django.db import models
from uuid import uuid4
from courses.models import Course
from users.models import User


class Purchase(models.Model):
    NOT_PAID = 'Not Paid'
    CANCELED = 'Canceled'
    CONFIRM = 'confirm'
    STATUS_CHOICES = [
        (NOT_PAID, 'Not Paid'),
        (CANCELED, 'Canceled'),
        (CONFIRM,'confirm'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=NOT_PAID)
    purchased_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.email} - {self.course.title}"
    

