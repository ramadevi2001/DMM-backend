from django.shortcuts import render

# Create your views here.
# goals/views.py
from rest_framework import generics,status
from rest_framework.response import Response
from .models import Goal
from .serializers import GoalSerializer

class GoalListCreateAPIView(generics.ListCreateAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

class GoalRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Record deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

