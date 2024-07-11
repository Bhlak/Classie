from django.urls import path
from .views import AnnouncementsAPIView, CommentsAPIView

urlpatterns = [
    
    path('announcements/', AnnouncementsAPIView.as_view()),
    path('comments/', CommentsAPIView.as_view())
]
