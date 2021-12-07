# Generated by Django 3.2 on 2021-12-06 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservedInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField()),
                ('booking_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation_info', to='listings.bookinginfo')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation_holder', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
