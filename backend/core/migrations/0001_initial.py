# Generated by Django 4.0.3 on 2022-04-08 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=128)),
                ('description', models.TextField(db_index=True)),
                ('floor', models.PositiveSmallIntegerField(db_index=True)),
                ('area_size', models.PositiveIntegerField(db_index=True)),
                ('price_per_month', models.DecimalField(db_index=True, decimal_places=7, max_digits=11)),
                ('number_of_rooms', models.PositiveSmallIntegerField(db_index=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=7, max_digits=11, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=7, max_digits=11, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Apartment',
                'verbose_name_plural': 'Apartments',
                'ordering': ['-id'],
            },
        ),
    ]
