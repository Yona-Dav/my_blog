from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import PostModelForm
from .models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostModelForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.likes = 5
        self.object.owner = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get(self, request, *args, **kwargs):
        print(request.user.is_authenticated)
        print(request.user)
        return super().get(request, *args, **kwargs)


class PostDetailView(DetailView):
    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostModelForm

class CommentCreateView(LoginRequiredMixin, CreateView):
    #Either
    model = Comment
    fields = ['content']
    template_name = 'post/post_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        post_id = self.kwargs['post_id']
        post = Post.objects.get(id=post_id)
        self.object.post = post
        self.object.save()
        return super().form_valid(form)
    # or
    # form_class =
    # success_url = reverse_lazy('', kwargs={'pk:})

    def get_success_url(self):
        return reverse_lazy('view_post',kwargs={'pk':self.object.post.id})


def my_post(request):
    return render(request, 'post/my_posts.html')
