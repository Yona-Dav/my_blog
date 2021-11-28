from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='homepage'),
    path('new_post', views.PostCreateView.as_view(), name='create_post'),
    path('new_post/<int:pk>', views.PostUpdateView.as_view(), name='edit_post'),
]