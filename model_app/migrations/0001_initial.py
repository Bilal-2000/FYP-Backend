# Generated by Django 4.2 on 2023-04-24 10:08

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
            name='PredictionsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('prediction_result', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='results')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
