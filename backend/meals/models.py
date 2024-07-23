from django.db import models
from django.contrib.auth.models import User

class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()
    calories = models.IntegerField()
    
    def __str__(self):
        return f"{self.name} - {self.date}"
    
    def calculate_total_calories(self):
        return sum(item.calories for item in self.food_items.all())

    def calculate_nutrition(self):
        # この例では簡単のために総カロリーのみを返していますが、
        # 実際にはタンパク質、脂質、炭水化物なども計算できます
        return {
            'total_calories': self.calculate_total_calories(),
        }

class FoodItem(models.Model):
    meal = models.ForeignKey(Meal, related_name='food_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    quantity = models.FloatField()
    unit = models.CharField(max_length=50)
    calories = models.IntegerField()
    
    def __str__(self):
        return f"{self.name} - {self.quantity} {self.unit}"