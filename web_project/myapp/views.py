from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, generics, status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from myapp.models import Category, CustomUser,Food, Order, OrderItem
from myapp.serializers import CategorySerializer, MyTokenObtainPairSerializer, OrderItemSerializer, OrderSerializer, ProfileSerializer, RegisterSerializer,FoodSerializer


#login user
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# register user
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer


class FoodView(APIView):
    # permission_classes = [AllowAny]
    def get_object(self, pk):
        try:
            return Food.objects.get(pk=pk)
        except Food.DoesNotExist:
            raise Http404
        
    def get(self, request):
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        # return render(request, 'foods.html', {'foods': foods})
        return Response({"Food":serializer.data})
    
    def get(self, request, pk, format=None):
        food = self.get_object(pk=pk)
        serializer = FoodSerializer(food)
        # return render(request, 'foods.html', {'foods': foods})
        return Response({"Food":serializer.data})
    
    def post(self, request):
        food = request.data
        serializer = FoodSerializer(data=food)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
    def put(self, request, pk, format=None):
        food = self.get_object(pk)
        serializer = FoodSerializer(food, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response({"Category":serializer.data})
    
    def post(self, request):
        category = request.data
        serializer = CategorySerializer(data=category)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response({"Order":serializer.data})
    # status code, data, message

class OrderItemView(APIView):
    def get(self, request):
        orderItems = OrderItem.objects.all()
        serializer = OrderItemSerializer(orderItems, many=True)
        return Response({"OrderItem":serializer.data})

# class FoodListView(APIView):

#     def get(self, request):
#         return Response({
#             "variety_food": ['1','2']
#         })

class FoodListCreateView(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class FoodDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = OrderItemSerializer

#api/profile
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfile(request):
    user = request.user
    serializer = ProfileSerializer(user, many = False)
    return Response(serializer.data)

#api/profile/update
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateProfile(request):
    user = request.user
    serializer = ProfileSerializer(user, data=request.data, partial= True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)