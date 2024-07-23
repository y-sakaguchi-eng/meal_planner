from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from meals.views import MealViewSet, FoodItemViewSet
from rest_framework.authtoken.views import obtain_auth_token
from accounts.views import RegisterView

router = DefaultRouter()
router.register(r'meals', MealViewSet, basename='meal')
router.register(r'fooditems', FoodItemViewSet, basename='fooditem') 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', obtain_auth_token, name='login'),
]
