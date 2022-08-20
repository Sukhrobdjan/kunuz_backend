from pipes import Template
from django.shortcuts import render

from helpers.models import BaseModels
from . serializers import TagSerializer,CategorySerializer,PostSerializer,RegionSerializer,TeamSerializer
from rest_framework.generics import ListCreateAPIView,ListAPIView
from .models import Post, Region,Tag,Category,Team
from helpers.pagination import CustomPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from django.utils.decorators import method_decorator



class TagView(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get('slug_title', None):
            queryset = queryset.filter(tag__slug=self.kwargs['slug_title'])

        return queryset
    
    @method_decorator(cache_page(60*60*2))
    @method_decorator(vary_on_headers("Authorization",))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class CategoryNewsView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]


    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get('slug_title', None):
            queryset = queryset.filter(category__slug=self.kwargs['slug_title'])

        return queryset

    @method_decorator(cache_page(60*60*2))
    @method_decorator(vary_on_headers("Authorization",))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class RegionNewsView(ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]


    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get('slug_title', None):
            queryset = queryset.filter(region__slug=self.kwargs['slug_title'])

        return queryset

    @method_decorator(cache_page(60*60*2))
    @method_decorator(vary_on_headers("Authorization",))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class PostView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    @method_decorator(cache_page(60*60*2))
    @method_decorator(vary_on_headers("Authorization",))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


        

class TeamListView(ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]


# IS_MAIN_NEWS
class IsMainNewsView(ListAPIView):
    queryset = Post.objects.filter(is_main=True)
    serializer_class = PostSerializer
    pagination_class = CustomPagination



# IS_EDITOR_CHOICE_NEWS  
class IsEditorChoiceNewsView(ListAPIView):
    queryset = Post.objects.filter(is_editor_choice=True)
    serializer_class = PostSerializer
    pagination_class = CustomPagination



# IS_TREND_NEWS
class IsTrendNewsView(ListAPIView):
    queryset = Post.objects.filter(is_trend=True)
    serializer_class = PostSerializer
    pagination_class = CustomPagination


# IS_INTERVIEW_NEWS
class IsInterviewNewsView(ListAPIView):
    queryset = Post.objects.filter(is_interview=True)
    serializer_class = PostSerializer
    pagination_class = CustomPagination


# IS_INVESTIGATION_NEWS
class IsInvestigationNewsView(ListAPIView):
    queryset = Post.objects.filter(is_investigation=True)
    serializer_class = PostSerializer
    pagination_class = CustomPagination

# IS_ARTICLE
class IsArticleNewsView(ListAPIView):
    queryset = Post.objects.filter(is_article=True)
    serializer_class = PostSerializer
    pagination_class = CustomPagination

# IS_BUSINESS
class IsArticleNewsView(ListAPIView):
    queryset = Post.objects.filter(is_business=True)
    serializer_class = PostSerializer
    pagination_class = CustomPagination


# IS_VIDEONEWS
class IsVideonewsNewsView(ListAPIView):
    queryset = Post.objects.filter(is_videonews=True)
    serializer_class = PostSerializer
    pagination_class = CustomPagination


# IS_PHOTONEWS:
class IsPhotoNewsView(ListAPIView):
    queryset = Post.objects.filter(is_photonews=True)
    serializer_class = PostSerializer
    pagination_class = CustomPagination


# IS_ADVICED:
class IsAdvicedNewsView(ListAPIView):
    queryset = Post.objects.filter(is_adviced=True)
    serializer_class = PostSerializer
    pagination_class = CustomPagination

