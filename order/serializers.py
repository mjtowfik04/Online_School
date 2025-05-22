from rest_framework import serializers
from .models import Enroll

class EnrollSerializer(serializers.ModelSerializer):
    Email = serializers.StringRelatedField(read_only=True)  # ইউজারের নাম দেখাবে, রিড-ওনলি
    course = serializers.StringRelatedField()  # কোর্সের টাইটেল দেখাবে

    class Meta:
        model = Enroll
        fields = ['id', 'Email', 'course', 'enrolled_at']
        read_only_fields = ['id', 'Email', 'enrolled_at']
