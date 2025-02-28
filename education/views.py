from tools.custom_pagination import CustomPagination
from education.models import Room, Subject, Level, Group
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from education.serializers import RoomSerializer, SubjectSerializer, LevelSerializer, GroupSerializer

class RoomsAPIView(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    pagination_class = CustomPagination

class RoomDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class SubjectsAPIView(ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    pagination_class = CustomPagination


class SubjectDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class LevelsAPIView(ListCreateAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    pagination_class = CustomPagination


class LevelDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class GroupAPIView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = CustomPagination


class GroupDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
