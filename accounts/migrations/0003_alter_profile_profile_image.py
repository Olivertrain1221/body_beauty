# Generated by Django 3.2 on 2022-03-26 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='/static/images/blank.jpg', upload_to='profile_pics'),
        ),
    ]
