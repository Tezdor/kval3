﻿# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class Booking(models.Model):
    user_id = models.IntegerField()
    quest_id = models.IntegerField()
    booking_status_id = models.IntegerField()
    payment_method_id = models.IntegerField()
    booking_date = models.DateTimeField()
    participants_count = models.IntegerField()
    cancellation_reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking'


class BookingStatus(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'booking_status'


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('QuestUser', models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PaymentMethod(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'payment_method'


class Quest(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    quest_type_id = models.IntegerField()
    difficulty_id = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    max_participants = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'quest'


class QuestDifficulty(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'quest_difficulty'


class QuestType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quest_type'


class QuestUser(models.Model):
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    login = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=20)
    registration_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quest_user'


class QuestUserGroups(models.Model):
    user = models.ForeignKey(QuestUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'quest_user_groups'
        unique_together = (('user', 'group'),)


class QuestUserUserPermissions(models.Model):
    user = models.ForeignKey(QuestUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'quest_user_user_permissions'
        unique_together = (('user', 'permission'),)


class User(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    registration_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
