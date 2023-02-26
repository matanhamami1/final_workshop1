# Generated by Django 4.1.2 on 2022-10-27 11:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('components', '0003_alter_component_options_alter_componentgroup_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=255)),
                ('visibility', models.BooleanField(default=False)),
                ('scheduled_at', models.DateTimeField()),
                ('end_at', models.DateTimeField()),
                ('status', models.CharField(choices=[('schedule', 'Scheduled'), ('in_progress', 'In Progress'), ('verifying', 'Verifying'), ('completed', 'Completed')], default='schedule', max_length=255)),
                ('impact', models.CharField(choices=[('maintenance', 'Maintenance')], default='maintenance', max_length=255)),
                ('components', models.ManyToManyField(blank=True, related_name='maintenances', to='components.component')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='maintenances', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='MaintenanceUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('text', models.CharField(max_length=1024)),
                ('new_status', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('schedule', 'Scheduled'), ('in_progress', 'In Progress'), ('verifying', 'Verifying'), ('completed', 'Completed')], max_length=255)),
                ('maintenance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maintenance_updates', to='maintenances.maintenance')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='maintenance_updates', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
    ]