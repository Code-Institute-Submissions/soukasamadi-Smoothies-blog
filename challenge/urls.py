from django.urls import path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static


"""url paths"""
urlpatterns = [
    path('challenge', views.challenge, name='challenge'),
    path('add_challenge/', views.Addchallenge.as_view(), name='add_challenge'),
    path('edit_challenge/<int:pk>', views.Editchallenge.as_view(), name='edit_challenge'),
    path('delete_challenge/<int:challenge_id>', views.delete_challenge, name='delete_challenge'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
                          