from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user_role']


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['hotel_image']


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['room_image']


class ReviewSerializer(serializers.ModelSerializer):
    user_name = UserProfileReviewSerializer()

    class Meta:
        model = Review
        fields = ['id', 'text', 'user_name', 'stars', 'user_name', 'hotel', 'parent']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class RoomListSerializer(serializers.ModelSerializer):
    room_images = RoomImageSerializer(read_only=True, many=True)

    class Meta:
        model = Room
        fields = ['room_number', 'room_type', 'room_status', 'room_price', 'room_images', 'all_inclusive']


class RoomDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'


class HotelListSerializer(serializers.ModelSerializer):
    hotel_image = HotelImageSerializer(read_only=True, many=True)

    class Meta:
        model = Hotel
        fields = ['hotel_name',  'country', 'city', 'hotel_image', 'hotel_stars']


class HotelDetailSerializer(serializers.ModelSerializer):
    hotel_image = HotelImageSerializer(read_only=True, many=True)
    reviews = ReviewSerializer(read_only=True, many=True)
    owner = UserProfileReviewSerializer()
    rooms = RoomListSerializer(read_only=True, many=True)

    class Meta:
        model = Hotel
        fields = ['hotel_name', 'description', 'country', 'city', 'address', 'hotel_stars', 'hotel_image',
                  'hotel_video', 'reviews', 'created_date', 'owner', 'rooms']
