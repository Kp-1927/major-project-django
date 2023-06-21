from django.contrib import admin
from .models import ProductBrandModel,ProductColorModel,ProductCategoryModel,ProductDescriptionModel,ProductImageModel,ProductMainModel,ProductModel,ProductServiceModel,ProductVariationModel

# Register your models here.
admin.site.register(ProductBrandModel)
admin.site.register(ProductColorModel)
admin.site.register(ProductCategoryModel)
admin.site.register(ProductDescriptionModel)
admin.site.register(ProductImageModel)
admin.site.register(ProductMainModel)
admin.site.register(ProductModel)
admin.site.register(ProductServiceModel)
admin.site.register(ProductVariationModel)
