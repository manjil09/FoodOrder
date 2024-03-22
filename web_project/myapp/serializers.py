from enum import unique
from unicodedata import category
from django.contrib.auth.models import Group, User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token

from myapp.models import CustomUser,Food,Category,Order,OrderItem

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user:CustomUser) -> Token:
        token = super().get_token(user)
        token['username'] = user.username
        token['email']= user.email
        return token

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required = True)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )

    class Meta:
        model = CustomUser
        fields = ['username','email','password','password2', 'bio']
    
    #remove and do validation from mobile
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            bio=validated_data['bio'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'
    
    def create(self, validated_data):
        return Food.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.food_name = validated_data.get('food_name', instance.food_name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.is_available = validated_data.get('is_available', instance.is_available)
        instance.image = validated_data.get('image', instance.image)
        instance.variety_options = validated_data.get('variety_options', instance.variety_options)
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.save()
        return instance

class CategorySerializer(serializers.ModelSerializer):
    # CategoryName = serializers.CharField(max_length=50)

    class Meta:
        model = Category
        fields = '__all__'
    
    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.category_name = validated_data.get('category_name',instance.category_name)
        instance.save()
        return instance

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        return Order.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id',instance.user_id)
        instance.order_date = validated_data.get('order_date',instance.order_date)
        instance.total_amount = validated_data.get('total_amount',instance.total_amount)
        instance.status = validated_data.get('status',instance.status)
        instance.save()
        return instance

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

    def create(self, validated_data):
        return OrderItem.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.order_id = validated_data.get('order_id',instance.order_id)
        instance.food_id = validated_data.get('food_id',instance.food_id)
        instance.quantity = validated_data.get('quantity',instance.quantity)
        instance.subtotal = validated_data.get('subtotal',instance.subtotal)
        instance.save()
        return instance