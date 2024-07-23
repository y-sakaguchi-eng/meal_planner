from rest_framework import viewsets, permissions
from .models import Meal, FoodItem
from .serializers import MealSerializer, FoodItemSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from datetime import timedelta
from django.utils import timezone


class MealViewSet(viewsets.ModelViewSet):
    serializer_class = MealSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Meal.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def weekly_report(self, request):
        end_date = timezone.now().date()
        start_date = end_date - timedelta(days=7)
        meals = Meal.objects.filter(user=request.user, date__range=[start_date, end_date])
        
        total_calories = meals.aggregate(Sum('calories'))['calories__sum'] or 0
        meal_count = meals.count()
        
        return Response({
            'start_date': start_date,
            'end_date': end_date,
            'total_calories': total_calories,
            'meal_count': meal_count,
            'average_calories_per_day': total_calories / 7 if total_calories else 0,
        })

class FoodItemViewSet(viewsets.ModelViewSet):
    serializer_class = FoodItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return FoodItem.objects.filter(meal__user=self.request.user)

    def perform_create(self, serializer):
        meal = Meal.objects.get(pk=self.request.data.get('meal'))
        if meal.user != self.request.user:
            raise permissions.PermissionDenied("You do not have permission to add food items to this meal.")
        serializer.save()