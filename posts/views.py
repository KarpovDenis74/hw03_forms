from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Post, Group
from .forms import PostForm


@login_required
def new_post(request):
    if request.method != 'POST':
        form = PostForm()
        return render(request, 'posts/new_post.html', {'form': form})
    form = PostForm(request.POST)
    if not form.is_valid():
        return render(request, 'posts/new_post.html', {'form': form})
    post = form.save(commit=False)
    post.author = request.user
    post.save()
    return redirect('index')


@login_required
def index(request):
    latest = Post.objects.all()[:11]
    return render(request, "index.html", {"posts": latest})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.post_group.all()[:12]
    return render(request, "group.html", {'group': group, 'posts': posts})
