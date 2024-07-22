from rest_framework import serializers
from .models import Meal, FoodItem

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ['id', 'name', 'quantity', 'unit', 'calories']

class MealSerializer(serializers.ModelSerializer):
    food_items = FoodItemSerializer(many=True, read_only=True)

    class Meta:
        model = Meal
        fields = ['id', 'name', 'description', 'date', 'calories', 'food_items']