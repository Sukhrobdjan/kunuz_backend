from rest_framework import serializers
from .models import Post,Tag,Category,Region,Team



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['title']

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['title']


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    region = RegionSerializer()
    tags = TagSerializer(many =True)
    class Meta:
        model = Post
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'