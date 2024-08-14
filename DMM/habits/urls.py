from django.urls import path
from .views import (
    HabitListCreateAPIView,
    HabitDetailAPIView,
    HabitByMonthlyGoalAPIView,
    HabitByDateAPIView,
)

urlpatterns = [
    path('habits/', HabitListCreateAPIView.as_view(), name='habit-list-create'),
    path('habits/<uuid:pk>/', HabitDetailAPIView.as_view(), name='habit-detail'),
    path('habits/monthly_goal/<uuid:monthly_goal_id>/', HabitByMonthlyGoalAPIView.as_view(), name='habit-by-monthly-goal'),
    path('habits/date/<str:date>/', HabitByDateAPIView.as_view(), name='habit-by-date'),
]
