from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Habit
from .serializers import HabitSerializer, HabitCreateSerializer, HabitUpdateSerializer
from django.utils.timezone import make_aware
from datetime import datetime

class HabitListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return HabitCreateSerializer
        return HabitSerializer

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(user=user)

class HabitDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(user=user)

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return HabitUpdateSerializer
        return HabitSerializer

    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.is_done:
            instance.productivity = self.calculate_productivity(
                instance.start_time,
                instance.end_time,
                instance.planned_period_minutes
            )
            instance.save()

    def calculate_productivity(self, start_time, end_time, planned_period_minutes):
        duration = (end_time - start_time).total_seconds() / 60  # in minutes
        return round(min(100, (duration / planned_period_minutes) * 100), 2)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Habit deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)

class HabitByMonthlyGoalAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        monthly_goal_id = self.kwargs['monthly_goal_id']
        return Habit.objects.filter(user=user, monthly_goal_id=monthly_goal_id)

class HabitByDateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, date):
        user = request.user
        date_obj = datetime.strptime(date, "%d-%m-%Y")
        start_date = make_aware(datetime.combine(date_obj, datetime.min.time()))
        end_date = make_aware(datetime.combine(date_obj, datetime.max.time()))
        habits = Habit.objects.filter(user=user, start_time__range=(start_date, end_date))
        serializer = HabitSerializer(habits, many=True)
        return Response(serializer.data)
