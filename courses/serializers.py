from rest_framework import serializers
from decimal import Decimal
from courses .models import Category,Course, Review,CourseImage
from django.contrib.auth import get_user_model


class CategorySerializer(serializers.ModelSerializer):
    course_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'course_count']


class CourseImageSerializer(serializers.ModelSerializer):
    image=serializers.ImageField()
    class Meta:
        model =CourseImage
        fields = ['id','image']


class CourseSerializer(serializers.ModelSerializer):
    images=CourseImageSerializer(many=True,read_only=True)
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'price', 'category','images']  

    
class SimpleUserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(
        method_name='get_current_user_name')

    class Meta:
        model = get_user_model()
        fields = ['id', 'name']

    def get_current_user_name(self, obj):
        return obj.get_full_name()


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(method_name='get_user')

    class Meta:
        model = Review
        fields = ['id', 'user', 'course', 'ratings', 'comment']
        read_only_fields = ['user', 'course']

    def get_user(self, obj):
        return SimpleUserSerializer(obj.user).data

    def create(self, validated_data):
        course_id = self.context['course_id']
        return Review.objects.create(course_id=course_id, **validated_data)
    
  
 