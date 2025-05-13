from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
# from cloudinary.models import CloudinaryField


class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class CategoryImage(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='category_images/')
    # image = CloudinaryField('image')



class Course(models.Model):
    title= models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="courses")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class CourseImage(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='images')
    # image = CloudinaryField('image')
    image = models.ImageField(upload_to='category_images/')


    

class Review(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    ratings = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Review by {self.user.first_name} on {self.course.title}"
