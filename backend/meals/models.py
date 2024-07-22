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

class FoodItem(models.Model):
    meal = models.ForeignKey(Meal, related_name='food_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    quantity = models.FloatField()
    unit = models.CharField(max_length=50)
    calories = models.IntegerField()
    
    def __str__(self):
        return f"{self.name} - {self.quantity} {self.unit}"