from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .forms import CommentForm

from .views import *

"""url paths"""
urlpatterns = [
    path('delete_comment/<int:comment_id>',
         views.delete_comment, name='delete_comment'),
    path('edit_comment/<int:pk>', views.EditComment.as_view(),
         name='edit_comment'),
    path('', views.index, name="index"),
    path('search/', views.search, name="search"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('blog/', views.BlogRecipe.as_view(), name="blog"),
    path('categories/', views.categories, name="categories"),
    path('categories_posts/<str:cats>',
         views.categories_view, name="categories_posts"),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
    # path('accounts/', include('allauth.urls')),
    path('profile', views.ProfileView, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
