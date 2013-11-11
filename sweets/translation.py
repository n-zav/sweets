from modeltranslation.translator import translator, TranslationOptions
from sweets.models import Product


class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'candies', 'pre_order')

translator.register(Product, ProductTranslationOptions)
