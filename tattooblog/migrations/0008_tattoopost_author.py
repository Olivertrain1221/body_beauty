# Generated by Django 3.2 on 2022-03-15 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tattooblog', '0007_remove_tattoopost_thumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='tattoopost',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]