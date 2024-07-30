from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Habit
from .serializers import HabitSerializer
from django.utils.timezone import now, localtime, make_aware
from datetime import datetime, timedelta

class HabitListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class HabitDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(user=user)

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
        # Parse the date string in the format 'YYYY-MM-DD'
        date_obj = datetime.strptime(date, "%d-%m-%Y")
        start_date = make_aware(datetime.combine(date_obj, datetime.min.time()))
        end_date = make_aware(datetime.combine(date_obj, datetime.max.time()))
        habits = Habit.objects.filter(user=user, start_time__range=(start_date, end_date))
        serializer = HabitSerializer(habits, many=True)
        return Response(serializer.data)
