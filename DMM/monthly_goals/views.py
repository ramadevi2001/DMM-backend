from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import MonthlyGoal
from .serializers import MonthlyGoalSerializer
from goals.models import Goal
from choices.models import Choice

class MonthlyGoalListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = MonthlyGoalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        choices = Choice.objects.filter(user=user)
        goals = Goal.objects.filter(choice__in=choices)
        return MonthlyGoal.objects.filter(goal__in=goals)

    def perform_create(self, serializer):
        user = self.request.user
        goal = serializer.validated_data['goal']
        if Goal.objects.filter(id=goal.id, choice__user=user).exists():
            serializer.save()
        else:
            raise PermissionDenied("You do not have permission to add a monthly goal for this goal.")

class MonthlyGoalDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MonthlyGoalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        choices = Choice.objects.filter(user=user)
        goals = Goal.objects.filter(choice__in=choices)
        return MonthlyGoal.objects.filter(goal__in=goals)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Record deleted successfully'}, status=status.HTTP_200_OK)

class MonthlyGoalsByGoalAPIView(generics.ListAPIView):
    serializer_class = MonthlyGoalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        goal_id = self.kwargs['goal_id']
        choices = Choice.objects.filter(user=user)
        # Ensure the goal belongs to the user's choices
        if Goal.objects.filter(id=goal_id, choice__in=choices).exists():
            return MonthlyGoal.objects.filter(goal__id=goal_id, goal__choice__in=choices)
        else:
            return MonthlyGoal.objects.none()

