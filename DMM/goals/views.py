# goals/views.py
from rest_framework import generics
from .models import Goal
from .serializers import GoalSerializer

class GoalListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = GoalSerializer

    def get_queryset(self):
        user_id  = self.context['request'].user
        return Goal.objects.filter(choice__user_id=user_id)

class GoalDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

class GoalByChoiceAPIView(generics.ListAPIView):
    serializer_class = GoalSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        choice_id = self.kwargs['choice_id']
        return Goal.objects.filter(choice__user_id=user_id, choice_id=choice_id)
