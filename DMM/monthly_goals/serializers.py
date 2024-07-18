# monthly_goals/serializers.py
from rest_framework import serializers
from .models import MonthlyGoal

class MonthlyGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyGoal
        fields = '__all__'
