from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View


from .models import *
from .forms import *


# Create your views here.


def index(request):
    """Show a list of posts from newest with links to post details"""
    posts = Post.objects.all().order_by('-created_at')
    ctx = {
        "posts": posts,
    }
    return render(request, 'index.html', ctx)


def show_post(request, id):
    """Show a details of post with selected id"""
    post = get_object_or_404(Post, pk=id)
    ctx = {
        "post": post,
    }
    return render(request, 'post.html', ctx)


class NewPostView(View):

    def get(self, request):
        """Show a form to create a new post"""
        form = NewPostForm
        ctx = {
            "form": form,
        }
        return render(request, 'new.html', ctx)

    def post(self, request):
        """Save a new post to database"""
        form = NewPostForm(request.POST)
        description = request.POST.get('description')
        if form.is_valid():
            f = form.save(commit=False)
            f.description = description
            f.save()
            return redirect(reverse("home"))



class EditPostView(View):

    def get(self, request, id):
        """Show a form to edit a post with selected id"""
        pass

    def post(self, request, id):
        """Save changes made to selected post to database"""
        pass


class DeletePostView(View):

    def get(self, request, id):
        """Show a form to delete a post with selected id"""

    def post(self, request, id):
        """Delete a selected post from database"""
        pass
