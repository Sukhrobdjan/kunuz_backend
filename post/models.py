from django.core.files.uploadedfile import UploadedFile
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from helpers.models import BaseModels
import mutagen



class Audio(BaseModels):
    title = models.CharField(max_length=128)
    track = models.FileField(upload_to='audio/')
    image = models.ImageField(upload_to='audio/image/')
    duration = models.PositiveIntegerField("audio duration in seconds", blank=True, null=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Audio)
def some_pre_save_receiver(sender, instance, raw, using, update_fields, **kwargs):
    file_was_updated = False
    if hasattr(instance.track, 'file') and isinstance(instance.track.file, UploadedFile):
        file_was_updated = True

    if update_fields and "track" in update_fields:
        file_was_updated = True

    if file_was_updated:
        # read audio file metadata
        audio_info = mutagen.File(instance.track).info
        # set audio duration in seconds, so we can access it in database
        instance.duration = int(audio_info.length)



class Category(BaseModels):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100,unique=True)

    class Meta:
        ordering = ['created_at']


    def __str__(self):
        return self.title




class Tag(BaseModels):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100,unique=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title


class Region(BaseModels):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100,unique=True)

    def __str__(self):
        return self.title


class Team(BaseModels):
    full_name = models.CharField(max_length=500)
    slug = models.SlugField(max_length=100,unique=True)
    job_title = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'team/')

    def __str__(self):
        return self.full_name

class Contact(BaseModels):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100,unique=True)
    email = models.CharField(max_length=200)
    phone_number = models.BigIntegerField(default=9989)
    theme = models.CharField(max_length=500)
    message = models.TextField()

    def __str__(self):
        return self.name



class Post(BaseModels):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100,unique=True)
    img = models.ImageField(upload_to = 'post/')
    caption = models.CharField(max_length=250)
    text =models.TextField()

    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null = True, related_name='posts')
    region = models.ForeignKey(Region,on_delete=models.SET_NULL,null = True,blank=True)
    views = models.BigIntegerField(default=0)
    tags = models.ManyToManyField(Tag, blank=True)

    is_main = models.BooleanField(default=False)
    is_editor_choice = models.BooleanField(default=False)
    is_trend = models.BooleanField(default=False)
    is_interview = models.BooleanField(default=False)
    is_investigation = models.BooleanField(default=False)
    is_article = models.BooleanField(default=False)
    is_business = models.BooleanField(default=False)
    is_videonews = models.BooleanField(default=False)
    is_photonews = models.BooleanField(default=False)
    is_adviced = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']
        
    def __str__(self):
        return self.title




