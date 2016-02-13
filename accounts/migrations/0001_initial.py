# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-13 02:57
from __future__ import unicode_literals

import django.db.models.deletion
import django_countries.fields
from django.conf import settings
from django.db import migrations, models

import accounts.fields


def create_user_profiles(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    UserProfile = apps.get_model('accounts', 'UserProfile')
    for user in User.objects.all():
        UserProfile.objects.create(user=user)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', accounts.fields.PhoneField(blank=True, max_length=15, null=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RunPython(create_user_profiles,
                             reverse_code=migrations.RunPython.noop),
    ]