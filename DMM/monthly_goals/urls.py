from django.urls import path
from .views import (
    MonthlyGoalListCreateAPIView,
    MonthlyGoalDetailAPIView,
    MonthlyGoalsByGoalAPIView
)

urlpatterns = [
    path('monthly_goals/', MonthlyGoalListCreateAPIView.as_view(), name='monthly-goal-list-create'),
    path('monthly_goals/<uuid:pk>/', MonthlyGoalDetailAPIView.as_view(), name='monthly-goal-detail'),
    path('monthly_goals/goal/<uuid:goal_id>/', MonthlyGoalsByGoalAPIView.as_view(), name='monthly-goals-by-goal'),
]
