from .models import User, Booking
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['full_name', 'phone', 'login', 'email', 'password1', 'password2']


class BookingForm(forms.ModelForm):
    booking_date = forms.DateTimeField(widget=forms.widgets.DateTimeInput(attrs={'type':'datetime-local'}))

    class Meta:
        model = Booking
        fields = ['quest', 'payment_method', 'booking_date', 'participants_count']
