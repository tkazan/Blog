from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *
from .forms import *


# Create your views here.


def index(request):
    """Show a list of posts from newest with links to post details."""
    post_list = Post.objects.all().order_by('-created_at')
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {"posts": posts})


def show_post(request, id):
    """Show a details of post with selected id."""
    post = get_object_or_404(Post, pk=id)
    ctx = {
        "post": post,
    }
    return render(request, 'post.html', ctx)


class NewPostView(View):

    def get(self, request):
        """Show a form to create a new post."""
        form = NewPostForm
        ctx = {
            "form": form,
        }
        return render(request, 'new.html', ctx)

    def post(self, request):
        """Save a new post to database."""
        form = NewPostForm(request.POST)
        description = request.POST.get('description')
        if form.is_valid():
            f = form.save(commit=False)
            f.description = description
            f.save()
            return redirect(reverse("home"))


class EditPostView(View):

    def get(self, request, id):
        """Show a form to edit a post with selected id."""
        post = get_object_or_404(Post, pk=id)
        ctx = {
            "post": post,
        }
        return render(request, "edit.html", ctx)

    def post(self, request, id):
        """Save changes made to selected post to database."""
        title = request.POST.get("title")
        description = request.POST.get("description")
        post = Post.objects.get(pk=id)
        try:
            post.title = title
            post.description = description
            post.save()
            return redirect(reverse("home"))
        except Exception as e:
            message = "Something went wrong: {}".format(e)
            ctx = {
                "message": message,
                "post": post,
            }
            return render(request, 'edit.html', ctx)


class DeletePostView(View):

    def get(self, request, id):
        """Show a form to delete a post with selected id."""
        post = get_object_or_404(Post, pk=id)
        ctx = {
            "post": post,
        }
        return render(request, "delete.html", ctx)

    def post(self, request, id):
        """Delete a selected post from database."""
        action = request.POST.get("submit")

        if action == "YES":
            post = Post.objects.get(pk=id)
            post.delete()
        return redirect(reverse("home"))
