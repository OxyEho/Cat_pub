from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('table/<int:pk>', views.booking_table, name='table-detail'),
    path('booking', views.booked_view, name='booked'),
    path('search', views.search_booking, name='search')
]
