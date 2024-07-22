from django.urls import path
from .views import GoalListCreateAPIView, GoalDetailAPIView, GoalByChoiceAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('goals/', GoalListCreateAPIView.as_view(), name='goal-list-create'),
    path('goals/<uuid:pk>/', GoalDetailAPIView.as_view(), name='goal-detail'),
    path('goals-choice/<uuid:choice_id>/', GoalByChoiceAPIView.as_view(), name='user-choice-goals'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
