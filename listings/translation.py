from modeltranslation.translator import register, TranslationOptions
from .models import Category, Info, Listing



@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)



@register(Info)
class InfoTranslationOptions(TranslationOptions):
    fields = ('info_name',)


@register(Listing)
class ListingTranslationOptions(TranslationOptions):
    fields = ('title', 'category', 'address', 'district', 'region', 'city', 'state', 'description', 'sale_and_rental', 'vid_name', 'tip_name' )




