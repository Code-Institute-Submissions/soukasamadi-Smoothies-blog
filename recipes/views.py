from django.views import generic, View
from .models import *
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


def CategoriesView(request, cats):
    """View to return the posts filtered by categories"""
    categories_posts = Post.objects.filter(categories__title__contains=cats)
    return render(request, 'categories_posts.html', {
        'cats': cats.title(), 'categories_posts': categories_posts})


class BlogRecipe(generic.ListView):
    """
    Renders the blog page
    """
    model = Recipe
    queryset = Recipe.objects.filter(status=1)
    template_name = 'recipes/blog.html'
    paginate_by = 6
