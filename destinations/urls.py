from django.urls import path
from .views import destinations_view, logout_view, destination_details_view, book_tour, payment_success, payment_page

urlpatterns = [
    path('', destinations_view, name='destinations'),
    path('logout/', logout_view, name='logout'),
    path('<str:country>/', destination_details_view, name='destination_details'),
    path('destinations/book/<str:country>/',book_tour, name='book_tour'),
    path('payment/<str:country>/', payment_page, name='payment_page'),
    path('payment-success/<str:country>/', payment_success, name='payment_success'),

]

