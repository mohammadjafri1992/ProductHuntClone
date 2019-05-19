from django.urls import path

from .views import create, home_view, detail, upvote

urlpatterns = [
    path('', home_view, name='home'),
    path('create/', create, name='create'),
    path('<int:product_id>', detail, name='detail'),
    path('<int:product_id>/upvote', upvote, name='upvote'),

]
