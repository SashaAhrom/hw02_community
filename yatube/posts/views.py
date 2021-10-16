from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request):
    """Passes the last ten Post model objects and title."""
    title = 'Последние обновления на сайте'
    posts = Post.objects.all()[:10]
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    """Passes the last ten Post model objects
    filtered by group field and title."""
    group = get_object_or_404(Group, slug=slug)
    posts = group.community.all()[:10]
    title = f'Записи сообщества {group}'
    context = {
        'group': group,
        'posts': posts,
        'title': title
    }
    return render(request, 'posts/group_list.html', context)
