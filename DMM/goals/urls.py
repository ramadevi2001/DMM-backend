# goals/urls.py
from django.urls import path
from .views import GoalListCreateAPIView, GoalRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('goals/', GoalListCreateAPIView.as_view(), name='goal-list-create'),
    path('goals/<uuid:pk>/', GoalRetrieveUpdateDestroyAPIView.as_view(), name='goal-retrieve-update-destroy'),
]
