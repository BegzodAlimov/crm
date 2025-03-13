from django.urls import path

from education.views import RoomsAPIView, RoomDetailAPIView, SubjectsAPIView, SubjectDetailAPIView, \
    GroupAPIView, GroupDetailAPIView, LevelsAPIView, LevelDetailAPIView

urlpatterns = [
    path('rooms/', RoomsAPIView.as_view(), name='rooms_list'),
    path('rooms/<int:pk>/', RoomDetailAPIView.as_view(), name='room_detail'),
    path('subjects/', SubjectsAPIView.as_view(), name='subjects_list'),
    path('subjects/<int:pk>/', SubjectDetailAPIView.as_view(), name='subject_detail'),
    path('groups/', GroupAPIView.as_view(), name='groups_list'),
    path('groups/<int:pk>/', GroupDetailAPIView.as_view(), name='group_detail'),
    path('levels/', LevelsAPIView.as_view(), name='levels_list'),
    path('levels/<int:pk>/', LevelDetailAPIView.as_view(), name='level_detail'),
]