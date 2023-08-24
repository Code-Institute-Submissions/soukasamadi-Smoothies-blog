from django.views import generic, View
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import *
from .forms import CommentForm, UserUpdateForm, ProfileUpdateForm
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import (
    render, get_object_or_404, reverse, redirect, resolve_url)
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    """
    Renders the index page
    """
    queryset = Recipe.objects.filter(
        featured=True, status=1).order_by('-timestamp')
    context = {
        'recipe_list': queryset,
    }
    return render(request, 'recipes/index.html', context)


class RecipeDetail(View):
    """
    Renders the post detail Page
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by("-timestamp")
        num_comments = Comment.objects.filter(recipe=recipe).count()
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipes/recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
                'num_comments': num_comments,
            },
        )

    def recipe(self, request, slug, *args, **kwargs):
        """
        Comment on the posts
        """
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by("-timestamp")
        liked = False

        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
            messages.success(request, """
            Your comment was sent successfully and is awaiting approval!""")
        else:
            comment_form = CommentForm()
        return render(
            request,
            "recipes/recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked,
            },
        )


class RecipeLike(View):
    """View for post like/Unlike"""

    def recipe(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
            messages.success(request, f"You have unliked this post.")
        else:
            recipe.likes.add(request.user)
            messages.success(request, f"You have liked this post, thanks!")
        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


def about(request):
    """View to return the about page"""
    return render(request, 'recipes/about.html')


def contact(request):
    """View to return the contact page"""
    return render(request, 'recipes/contact.html')


def categories(request):
    """View to return the categories page"""
    return render(request, 'recipes/categories.html')


def categories_view(request, cats):
    """
    Renders the posts filtered by categories
    """
    categories_posts = Recipe.objects.filter(
        categories__title__contains=cats, status=1)
    return render(request, 'recipes/categories_posts.html', {
        'cats': cats.title(), 'categories_posts': categories_posts})


def ProfileView(request):
    """View to return the profile page"""
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                         request.FILES,
                                         instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'recipes/profile.html', context)


def search(request):
    """search results"""
    queryset = Recipe.objects.all()
    if request.method == "POST":
        searched = request.POST["searched"]
        results = Recipe.objects.filter(
            Q(title__contains=searched) |
            Q(overview__icontains=searched) |
            Q(content__icontains=searched)
        ).distinct()
        context = {
            'queryset': queryset
        }

        return render(request, 'recipes/search.html', {
            'results': results, 'searched': searched})
    else:

        return render(request, 'recipes/search.html', context)


class BlogRecipe(generic.ListView):
    """
    Renders the blog page
    """
    model = Recipe
    queryset = Recipe.objects.filter(status=1)
    template_name = 'recipes/blog.html'
    paginate_by = 6

    def get_context_data(self, *args, **kwargs):
        categories_list = Category.objects.all()
        context = super(BlogRecipe, self).get_context_data(*args, **kwargs)
        context["categories_list"] = categories_list
        return context


def delete_comment(request, comment_id):
    """Delete comment"""
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    messages.success(request, 'Your comment was deleted successfully')
    return HttpResponseRedirect(reverse(
        'recipe_detail', args=[comment.recipe.slug]))


class EditComment(SuccessMessageMixin, UpdateView):
    """Edite comment"""
    model = Comment
    template_name = 'edit_comment.html'
    form_class = CommentForm
    success_message = 'The comment was successfully updated'
