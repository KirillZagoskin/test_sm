from django.contrib.auth import get_user_model, authenticate, login
from django.shortcuts import redirect, render
from django.views import View

from .forms import SignUpForm


User = get_user_model()

class SingUp(View):
    model_form = SignUpForm
    template = 'users/sign_up.html'

    def get(self, request, user_link):
        user = self._get_user(user_link)
        if user:
            context = {
                'form':self.model_form(instance=user),
                'link':user_link,
            }
            return render(request, self.template, context)
        return redirect('home_url')
    def post(self, request, user_link):

        user = self._get_user(user_link)
        bound_form = self.model_form(request.POST, instance=user)
        print(bound_form)
        if bound_form.is_valid():
            bound_form.save()
            password = bound_form.cleaned_data.get('password2')
            user = authenticate(request, username=user.username, password=password)
            login(request, user)
            user.link = None
            user.save()
            return redirect(user)
        return render(request, self.template, context={'form': bound_form, 'link':user_link,})


    def _get_user(self, user_link):
        try:
            user = User.objects.get(link=user_link)
        except:
            user = None
        return user


