from rest_framework import serializers
from education.models import Group, Room, Subject, Level
from tools.utility import validate_text
from users.models import User


class UserEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "middle_name"]


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["id", "room_number"]


class SubjectSerializer(serializers.ModelSerializer):
    teacher = UserEducationSerializer(many=True, read_only=True)
    class Meta:
        model = Subject
        fields = ["id", "subject_name", 'teacher']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ["id", "level_name"]


class GroupSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ["id", "subject_name"]


class GroupSerializer(serializers.ModelSerializer):
    group_name = serializers.CharField(max_length=50, validators=[validate_text])
    period = serializers.CharField(max_length=50, validators=[validate_text])
    price = serializers.IntegerField(min_value=1, max_value=100000000)
    teacher = UserEducationSerializer(read_only=True)
    students = UserEducationSerializer(read_only=True, many=True)
    subject = GroupSubjectSerializer()
    level = LevelSerializer()
    class Meta:
        model = Group
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')


class GroupCreateSerializer(serializers.ModelSerializer):
    group_name = serializers.CharField(max_length=50, validators=[validate_text])
    period = serializers.CharField(max_length=50, validators=[validate_text])
    price = serializers.IntegerField(min_value=1, max_value=100000000)

    class Meta:
        model = Group
        fields = '__all__'
