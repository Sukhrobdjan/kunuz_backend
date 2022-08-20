from modeltranslation.translator import translator, TranslationOptions
from .models import Category,Post,Tag

class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)
translator.register(Post, PostTranslationOptions)

    
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)
translator.register(Category, CategoryTranslationOptions)


class TagTranslationOptions(TranslationOptions):
    fields = ('title',)
translator.register(Tag, TagTranslationOptions)
