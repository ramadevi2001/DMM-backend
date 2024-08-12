from rest_framework import serializers
from .models import Observation

class ObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observation
        fields = ['id', 'observation', 'action_plan']
        
    def validate(self, data):
        user = self.context['request'].user
        observation = data['observation']
        
        if Observation.objects.filter(user=user, observation=observation).exists():
            raise serializers.ValidationError("An observation with this text already exists for the user.")
        
        return data
