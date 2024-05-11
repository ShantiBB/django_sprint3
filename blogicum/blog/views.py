from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from django.utils import timezone


def posts():
    posts_model = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )
    return posts_model


def index(request):
    template = 'blog/index.html'
    post_list = posts().order_by('-pub_date', 'title')[:5]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post = get_object_or_404(posts(), pk=id)
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category.objects.values(
            'title', 'description'
        ).filter(is_published=True),
        slug=category_slug
    )
    post_list = posts().filter(
        category__title=category['title']
    ).order_by('-pub_date', 'title')
    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, template, context)
