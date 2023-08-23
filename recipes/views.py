from django.views import generic, View
from .models import *
from django.db.models import Q
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from .forms import CommentForm, UserUpdateForm, ProfileUpdateForm
from django.shortcuts import (
    render, get_object_or_404, reverse, redirect, resolve_url)


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

    def get_context_data(self, *args, **kwargs):
        categories_list = Category.objects.all()
        context = super(RecipeDetail, self).get_context_data(*args, **kwargs)
        context["categories_list"] = categories_list
        return context


class RecipeLike(View):
    """View for post like/Unlike"""

    def recipe(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)
        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


def about(request):
    """View to return the about page"""
    categories = Category.objects.all()
    context = {
        'categories_list': categories
    }
    return render(request, 'recipes/about.html', context)


def contact(request):
    """View to return the contact page"""
    categories = Category.objects.all()
    context = {

        'categories_list': categories
    }

    return render(request, 'recipes/contact.html', context)


def categories(request):
    """View to return the categories page"""
    categories = Category.objects.all()
    context = {
        'categories_list': categories
    }
    return render(request, 'recipes/categories.html', context)


def categories_view(request, cats):
    """
    Renders the posts filtered by categories
    """
    categories = Category.objects.all()
    context = {
        'categories_list': categories
    }
    categories_posts = Recipe.objects.filter(
        categories__title__contains=cats, status=1)
    return render(request, 'recipes/categories_posts.html', {
        'cats': cats.title(), 'categories_posts': categories_posts})


def search(request):
    """search results"""
    queryset = Post.objects.all()
    if request.method == "POST":
        searched = request.POST["searched"]
        results = Post.objects.filter(
            Q(title__contains=searched) |
            Q(overview__icontains=searched) |
            Q(content__icontains=searched)
        ).distinct()
        context = {
            'queryset': queryset
        }

        return render(request, 'search.html', {
            'results': results, 'searched': searched})
    else:

        return render(request, 'search.html', context)


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
