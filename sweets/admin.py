from django.contrib import admin
from sweets.models import Product
from modeltranslation.admin import TranslationAdmin


class ProductAdmin(TranslationAdmin):
    pass

admin.site.register(Product, ProductAdmin)
