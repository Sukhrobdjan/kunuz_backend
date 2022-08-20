from django.urls import path
from .views import CategoryView,TagView,RegionView,PostView

urlpatterns = [
    path('cat/<slug:slug>',CategoryView.as_view()),
    path('tag/<slug:slug>',TagView.as_view()),
    path('reg/<slug:slug>',RegionView.as_view()),
    path('post/<slug:slug>',PostView.as_view()),

] 
