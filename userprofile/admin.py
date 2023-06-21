from django.contrib import admin
from .models import UserAddressModel,UserCartModel,UserProfileModel,UserWishListModel
# Register your models here.

admin.site.register(UserAddressModel)
admin.site.register(UserCartModel)
admin.site.register(UserProfileModel)
admin.site.register(UserWishListModel)
