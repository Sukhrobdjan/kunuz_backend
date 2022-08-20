from django.urls import path
from . views import IsEditorChoiceNewsView,PostView,CategoryNewsView,RegionNewsView\
    ,TagNewsView,TeamListView,IsMainNewsView,IsPhotoNewsView,IsInvestigationNewsView\
    ,IsAdvicedNewsView,IsArticleNewsView,IsInterviewNewsView,IsTrendNewsView,IsVideonewsNewsView,AudioListView



urlpatterns = [
    path('news/',PostView.as_view()),
    path('news/category/<slug:slug_name>/',CategoryNewsView.as_view()),
    path('news/region/<slug:slug_name>/', RegionNewsView.as_view()),
    path('news/tag/<slug:slug_name>/', TagNewsView.as_view()),
    path('team/', TeamListView.as_view()),
    path('audio/', AudioListView.as_view()),

    path('news/editor-choice/', IsEditorChoiceNewsView.as_view(), name="is_editor_choice"),
    path('news/trend/', IsMainNewsView.as_view(), name="is_main"),
    path('news/photo/', IsPhotoNewsView.as_view(), name="is_photo"),
    path('news/invest/', IsInvestigationNewsView.as_view(), name="is_innvest"),
    path('news/advice/', IsAdvicedNewsView.as_view(), name="is_advice"),
    path('news/article/', IsArticleNewsView.as_view(), name="is_article"),
    path('news/interviews/', IsInterviewNewsView.as_view(), name="is_article"),
    path('news/trend/', IsTrendNewsView.as_view(), name="is_trend"),
    path('news/vedio/', IsVideonewsNewsView.as_view(), name="is_vedio"),


] 


