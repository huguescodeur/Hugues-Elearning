# Generated by Django 5.0.1 on 2024-02-05 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='medias/images_root/user_profil/default_image.png', upload_to='medias/images_root/user_profil/'),
        ),
    ]
