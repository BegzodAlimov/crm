from rest_framework import serializers

from education.models import Course, Room, Subject, Level
from tools.utility import validate_text


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"
        read_only_fields = ['id', 'created_at', 'updated_at']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"
        read_only_fields = ['id', 'created_at', 'updated_at']

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = "__all__"
        read_only_fields = ['id', 'created_at', 'updated_at']


class CourseSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(max_length=50, validators=[validate_text])
    period = serializers.CharField(max_length=50, validators=[validate_text])
    price = serializers.IntegerField(min_value=1, max_value=100000000, validators=[validate_text])
    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')