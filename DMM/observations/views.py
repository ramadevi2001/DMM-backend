from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Observation
from .serializers import ObservationSerializer

class ObservationListCreateView(generics.ListCreateAPIView):
    serializer_class = ObservationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter observations by the currently authenticated user
        return Observation.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically set the user field to the currently authenticated user
        serializer.save(user=self.request.user)

class ObservationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ObservationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter observations by the currently authenticated user
        return Observation.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        # Call the superclass's delete method
        response = super().delete(request, *args, **kwargs)
        # Return a custom success message
        return Response({"message": "Observation successfully deleted."}, status=status.HTTP_204_NO_CONTENT)
