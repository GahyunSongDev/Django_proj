from django.urls import path
from .views import (
    HomeView,
    StudyView,
    DailyView,
    StudyDetailView,
    DailyDetailView,
    AddPostView,
    UpdatePostView,
    DeletePostView,
    ContactsView,
)

urlpatterns = [
    #url for class-based view
    path('', HomeView.as_view(), name="home"),
    
    #url for the study-blog view
    path('studyblog/', StudyView.as_view(), name="study-blog"),
    # URL for a study article within the studyBlog
    path('studyblog/article/<int:pk>/', StudyDetailView.as_view(), name='studyblog-article-detail'),
    # urls for the study update post
    path('studyblog/article/edit/<int:pk>/', UpdatePostView.as_view(), name='study_update_post'),

    # url for the daily-blog view
    path('dailyblog/', DailyView.as_view(), name="daily-blog"),
    # url for a daily article within the daily Blog
    path('dailyblog/article/<int:pk>/', DailyDetailView.as_view(), name='dailyblog-article-detail'),
    # urls for the daily update post
    path('dailyblog/article/edit/<int:pk>/', UpdatePostView.as_view(), name='daily_update_post'),
    
    # url for the create post view
    path('add_post/', AddPostView.as_view(), name='add_post',),

    # url for deleting the post
    path('post/delete/<int:pk>/', DeletePostView.as_view(), name='delete_post'),

    # url for the contacts page
    path('contacts/', ContactsView.as_view(), name='contacts'),
]   