from rest_framework import serializers
from .models import Habit

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = [
            'id', 'monthly_goal', 'title', 'description', 
            'planned_period_minutes', 'location', 'start_time', 'end_time', 'productivity'
        ]
