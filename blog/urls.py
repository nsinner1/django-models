from django.urls import path
from .views import HomePageView, PostDetailPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('blog/<int:pk>', PostDetailPageView.as_view(), name='blog')
]
