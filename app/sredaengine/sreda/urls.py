from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views


urlpatterns = [
    path('', views.main, name='home_url'),
    path('<str:username>', views.user_page, name='user_page'),
    path('questions/', views.questions, name='questions_url'),
    path('communities/', views.communities, name='communities_url'),
    path('post/<str:slug>/', views.PostDetail.as_view(), name='post_detail_url'),
    ]