# Generated by Django 3.2 on 2022-03-26 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='https://res.cloudinary.com/dxsodecl1/image/upload/v1648314484/blank-profile-picture-973460_640_vcmm3c.webp', upload_to='profile_pics'),
        ),
    ]
