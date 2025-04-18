from django.shortcuts import render
from .forms import RegisterForm, BookingForm
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from .models import Quest, Booking, BookingStatus
from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = '/login/'
    template_name = 'users/register.html'


class BookingView(CreateView, LoginRequiredMixin):
    form_class = BookingForm
    success_url = '/bookings_list/'
    template_name = 'booking.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.booking_status = BookingStatus.objects.get(id=1)
        return super().form_valid(form)


@login_required
def index(request):
    quests = Quest.objects.all()
    return render(request, template_name='dashboard.html', context={'quests': quests})


@login_required
def bookings_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, template_name='bookings_list.html', context={'bookings': bookings})
