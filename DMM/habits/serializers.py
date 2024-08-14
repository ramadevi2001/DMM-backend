from rest_framework import serializers
from .models import Habit
from datetime import timedelta

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'

class HabitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = [
            'monthly_goal', 'title', 'description', 
            'planned_period_minutes', 'location', 'start_time'
        ]

    def validate(self, data):
        user = self.context['request'].user
        start_time = data['start_time']
        planned_period_minutes = data['planned_period_minutes']
        end_time = start_time + timedelta(minutes=planned_period_minutes)

        # Check for any habit that overlaps with the given time period
        if Habit.objects.filter(
            user=user,
            start_time__lt=end_time,  # Other habit starts before the new habit ends
            end_time__gt=start_time   # Other habit ends after the new habit starts
        ).exists():
            raise serializers.ValidationError("You already have an ongoing habit during this time period.")

        return data

    def create(self, validated_data):
        user = self.context['request'].user
        start_time = validated_data.get('start_time')
        planned_period_minutes = validated_data.get('planned_period_minutes')
        end_time = start_time + timedelta(minutes=planned_period_minutes)
        
        habit = Habit.objects.create(
            user=user,  # Set the user field
            **validated_data,
            end_time=end_time,
            productivity=0,  # Initially set to 0
            is_done=False    # Initially set to not done
        )
        return habit

class HabitUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = [
            'id', 'monthly_goal', 'title', 'description', 
            'planned_period_minutes', 'location', 'start_time', 
            'end_time', 'is_done'
        ]

    def update(self, instance, validated_data):
        # Update all the fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # Calculate end time and productivity only when is_done is True
        if validated_data.get('is_done', instance.is_done):
            # Ensure end_time is provided
            if 'end_time' in validated_data:
                instance.productivity = self.calculate_productivity(
                    instance.start_time,
                    instance.end_time,
                    instance.planned_period_minutes
                )
            else:
                raise serializers.ValidationError("End time must be provided when marking habit as done.")
        
        instance.save()
        return instance

    def calculate_productivity(self, start_time, end_time, planned_period_minutes):
        actual_duration_minutes = (end_time - start_time).total_seconds() / 60
        return round(min(100, (actual_duration_minutes / planned_period_minutes) * 100), 2)
