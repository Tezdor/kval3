from django.urls import path
from .views import RegisterView, index, bookings_list, BookingView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view(template_name='users/login.html')),
    path('logout/', LogoutView.as_view(template_name='users/logout.html')),
    path('', index, name='base'),
    path('bookings_list/', bookings_list, name='bookings_list'),
    path('booking/', BookingView.as_view()),
]