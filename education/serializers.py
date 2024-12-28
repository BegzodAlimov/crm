from rest_framework import serializers

from education.models import Course
from tools.utility import validate_text


class RoomSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    room_number = serializers.IntegerField(min_value=1, max_value=9999)

class SubjectSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    subject_name = serializers.CharField(max_length=50, validators=[validate_text])

class LevelSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    level_name = serializers.CharField(max_length=50, validators=[validate_text])


class CourseSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(max_length=50, validators=[validate_text])
    period = serializers.CharField(max_length=50, validators=[validate_text])
    price = serializers.IntegerField(min_value=1, max_value=100000000, validators=[validate_text])
    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')