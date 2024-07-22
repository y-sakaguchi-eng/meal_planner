from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from meals.views import MealViewSet, FoodItemViewSet

router = DefaultRouter()
router.register(r'meals', MealViewSet, basename='meal')
router.register(r'fooditems', FoodItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
