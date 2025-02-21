from django.urls import path

from education.views import RoomsAPIView, RoomDetailAPIView, SubjectsAPIView, SubjectDetailAPIView, \
    CourseAPIView, CourseDetailAPIView, LevelsAPIView, LevelDetailAPIView

urlpatterns = [
    path('rooms/', RoomsAPIView.as_view(), name='rooms_list'),
    path('rooms/<uuid:pk>/', RoomDetailAPIView.as_view(), name='room_detail'),
    path('subjects/', SubjectsAPIView.as_view(), name='subjects_list'),
    path('subjects/<uuid:pk>/', SubjectDetailAPIView.as_view(), name='subject_detail'),
    path('courses/', CourseAPIView.as_view(), name='courses_list'),
    path('courses/<uuid:pk>/', CourseDetailAPIView.as_view(), name='course_detail'),
    path('levels/', LevelsAPIView.as_view(), name='levels_list'),
    path('levels/<uuid:pk>/', LevelDetailAPIView.as_view(), name='level_detail'),
]