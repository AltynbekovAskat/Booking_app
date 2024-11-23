from xml.etree.ElementInclude import include
from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'Users', UserProfileViewSet, basename='user_list')
router.register(r'Hotel', HotelListViewSet, basename='hotel_list')
router.register(r'Hotel_Detail', HotelDetailViewSet, basename='hotel_detail')
router.register(r'Hotel_img', HotelImageViewSet, basename='hotel_img_list')
router.register(f'Room', RoomListViewSet, basename='room_list')
router.register(r'RoomDetail', RoomDetailViewSet, basename='room_detail')
router.register(r'Room_img', RoomImageViewSet, basename='room_img_list')
router.register(r'Review', ReviewViewSet, basename='review_list')
router.register(r'Booking', BookingViewSet, basename='booking_list')

urlpatterns = [
    path('', include(router.urls))
]
