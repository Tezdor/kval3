from django.db import models
from django.contrib.auth.models import AbstractUser


class Booking(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    quest = models.ForeignKey('Quest', on_delete=models.CASCADE)
    booking_status = models.ForeignKey('BookingStatus', on_delete=models.CASCADE)
    payment_method = models.ForeignKey('PaymentMethod', on_delete=models.CASCADE)
    booking_date = models.DateTimeField()
    participants_count = models.IntegerField()
    cancellation_reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking'

    def __str__(self):
        return str(self.id)


class BookingStatus(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'booking_status'

    def __str__(self):
        return self.name


class PaymentMethod(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'payment_method'

    def __str__(self):
        return self.name


class Quest(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    quest_type = models.ForeignKey('QuestType', on_delete=models.CASCADE)
    difficulty = models.ForeignKey('QuestDifficulty', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    max_participants = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'quest'

    def __str__(self):
        return self.name


class QuestDifficulty(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'quest_difficulty'

    def __str__(self):
        return self.name


class QuestType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quest_type'

    def __str__(self):
        return self.name


class User(AbstractUser):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    login = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=20, blank=True)
    registration_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    REQUIRED_FIELDS = ['full_name', 'phone', 'email', 'password', 'username']
    USERNAME_FIELD = 'login'

    def __str__(self):
        return self.full_name
