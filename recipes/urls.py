from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .forms import CommentForm

from .views import *

"""url paths"""
urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('blog/', views.BlogRecipe.as_view(), name="blog"),
    path('categories/', views.categories, name="categories"),
    path('categories_posts/<str:cats>',
         views.CategoriesView, name="categories_posts"),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
