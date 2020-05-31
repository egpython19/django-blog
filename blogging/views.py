from django.shortcuts import render, redirect
from django.http import Http404
from blogging.models import Post
from blogging.forms import MyPostForm


def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    context = {'posts': posts}
    return render(request, 'blogging/list.html', context)


def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}
    return render(request, 'blogging/detail.html', context)


def add_model(request):
    if request.method == "POST":
        form = MyPostForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.author = request.user
            model_instance.save()
            return redirect('/')
    else:  # GET
        form = MyPostForm()
        context = {'form': form}
        return render(request, "blogging/add.html", context)
