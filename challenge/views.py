from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Challenge
from .forms import ChallengeForm
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def challenge(request):
    """
    Renders the challenge page
    """
    challenge_list = Challenge.objects.all().filter(
        approved=True).order_by("-timestamp")
    return render(request, 'challenge/challenge.html', {'challenge_list': challenge_list})


class AddChallenge(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Add Challenge
    """
    model = Challenge
    form_class = ChallengeForm
    template_name = 'challenge/add_challenge.html'
    success_message = """Thank you for sharing your experience !<br>
    your post is awaiting approval!"""

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)


class EditChallenge(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Edit Challenge
    """
    model = Challenge   
    form_class = ChallengeForm
    template_name = 'challenge/add_challenge.html'
    success_message = 'Your post was successfully updated !'


def delete_challenge(request, challenge_id):
    """
    Delete challenge
    """
    challenge = get_object_or_404(Challenge, id=challenge_id)
    challenge.delete()
    messages.success(request, 'The post was deleted successfully')
    return redirect('challenge')