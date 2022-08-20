from django.contrib import admin
from .models import Post,Category,Region,Tag,Contact,Team,AudioFile



class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}  # new

admin.site.register(Tag, TagAdmin)


class AudioFiledAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}  # new

admin.site.register(AudioFile, AudioFiledAdmin)


class CategoyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}  # new

admin.site.register(Category, CategoyAdmin)


class RegionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}  # new

admin.site.register(Region, RegionAdmin)



class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}  # new

admin.site.register(Post, PostAdmin)


class TeamAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("full_name",)}  # new

admin.site.register(Team, TeamAdmin)


class ContactAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}  # new

admin.site.register(Contact, ContactAdmin)