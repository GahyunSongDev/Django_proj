from django.urls import path
from .views import (
    HomeView,
    StudyView,
    DailyView,
    StudyDetailView,
    DailyDetailView,
    AddPostView,
)

urlpatterns = [
    #url for class-based view
    path('', HomeView.as_view(), name="home"),
    
    #url for the study-blog view
    path('studyblog/', StudyView.as_view(), name="study-blog"),
    # URL for a study article within the studyBlog
    path('studyblog/article/<int:pk>/', StudyDetailView.as_view(), name='studyblog-article-detail'),

    #url for the daily-blog view
    path('dailyblog/', DailyView.as_view(), name="daily-blog"),
    # URL for a daily article within the daily Blog
    path('dailyblog/article/<int:pk>/', DailyDetailView.as_view(), name='dailyblog-article-detail'),

    path('add_post/', AddPostView.as_view(), name='add_post',)
]   