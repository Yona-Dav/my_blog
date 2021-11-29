from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='homepage'),
    path('new_post', views.PostCreateView.as_view(), name='create_post'),
    path('new_post/<int:pk>', views.PostUpdateView.as_view(), name='edit_post'),
    path('view_post/<int:pk>', views.PostDetailView.as_view(), name='view_post'),
    path('comment/create/<int:post_id>/', views.CommentCreateView.as_view(), name='new_comment'),
    path('posts/mine', views.my_post, name='my_post'),

]