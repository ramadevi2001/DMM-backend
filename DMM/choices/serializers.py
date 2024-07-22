# choices/serializers.py
from rest_framework import serializers
from .models import Choice

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'become','user']
        read_only_fields = ['id','user']

    def validate(self, data):
        user = self.context['request'].user
        become = data.get('become')

        if Choice.objects.filter(become=become, user=user).exists():
            raise serializers.ValidationError("The combination of 'become' and 'user' must be unique.")

        return data

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)
