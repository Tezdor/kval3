from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Booking)
admin.site.register(PaymentMethod)
admin.site.register(Quest)
