# monthly_goals/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MonthlyGoalViewSet

router = DefaultRouter()
router.register(r'monthly_goals', MonthlyGoalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
