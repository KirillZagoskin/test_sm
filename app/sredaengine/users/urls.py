from django.urls import path, include

from .views import SingUp


urlpatterns = [
    path('<user_link>', SingUp.as_view(), name='sing_up')
]