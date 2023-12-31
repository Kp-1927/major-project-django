# Generated by Django 4.2.2 on 2023-06-21 05:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userprofile', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofilemodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='UserProfileModel_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userprofilemodel',
            name='wishlist',
            field=models.ManyToManyField(blank=True, related_name='UserProfileModel_wishlist', to='userprofile.userwishlistmodel'),
        ),
        migrations.AddField(
            model_name='usercartmodel',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='UserCartModel_products', to='products.productmainmodel'),
        ),
    ]
