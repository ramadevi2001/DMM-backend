from django.shortcuts import render

# Create your views here.
# monthly_goals/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import MonthlyGoal
from .serializers import MonthlyGoalSerializer

class MonthlyGoalViewSet(viewsets.ModelViewSet):
    queryset = MonthlyGoal.objects.all()
    serializer_class = MonthlyGoalSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Record deleted successfully"}, status=status.HTTP_200_OK)

