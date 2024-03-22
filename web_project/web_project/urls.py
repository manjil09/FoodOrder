"""
URL configuration for web_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import imp
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from myapp import views
from rest_framework_simplejwt import views as jwt_views
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
# router.register(r'foods',views.FoodListCreateView,basename='food')

urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),

    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),

    path('profile/', views.getProfile, name='profile'),

    path('foods/',views.FoodView.as_view(),name='food_list'),
    
    path('foods/<int:pk>/',views.FoodView.as_view(),name='food_update'),
    
    path('categories/',views.CategoryView.as_view(),name='category_list'),
    
    path('orders/',views.OrderView.as_view(),name='order_detail'),
    
    path('orderitems/',views.OrderView.as_view(),name='orderitem_detail'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += router.urls