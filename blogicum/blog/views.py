from django.shortcuts import render, get_object_or_404

from blog.models import Post, Category


def index(request):
    template = 'blog/index.html'
    post_list = Post.published.all()[:5]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post = get_object_or_404(Post.published.all(), pk=id)
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category.objects.filter(is_published=True),
        slug=category_slug
    )
    post_list = Post.published.all().filter(category=category)
    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, template, context)
