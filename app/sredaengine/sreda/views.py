from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import get_user_model
from django.shortcuts  import get_object_or_404

from .utils import ObjectDetailMixin
from .models import Post, Questions, User


User = get_user_model()


def main(request):
    posts = Post.objects.all()
    return render(request, 'sreda/index.html', context={ 'tab_main': 'active', 'posts': posts,})

def questions(request):
    questions = Questions.objects.all()
    return render(request, 'sreda/questions.html', {'tab_questions': 'active', 'questions': questions})

def communities(request):
    posts = Post.objects.all()
    return render(request, 'sreda/communities.html', {'tab_communities': 'active', 'posts': posts})

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'sreda/post_detail.html'


def user_page(request, username):
    user = get_object_or_404(User, username__iexact=username)
    return render(request, 'sreda/user.html', {'user': user})



# class PostDetail(ObjectDetailMixin, View):
#     model = User
#     template = 'sreda/user_detail.html'






