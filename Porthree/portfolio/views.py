from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from MainApp.models import UserDetails, Project, Skill, Post, Comment
from django.http import JsonResponse
from .forms import CommentForm
from django.template.loader import render_to_string


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(parent_comment__isnull=True)
    user = request.user

    try:
        # Check if data already exists for the current user
        user_details = UserDetails.objects.get(user=user)
    except (UserDetails.DoesNotExist, TypeError):
      user_details = None

    if request.method == 'POST': # handle comments and replies
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user

            parent_comment_id = request.POST.get('parent_comment_id')
            if parent_comment_id:
                parent_comment = Comment.objects.get(id=parent_comment_id)
                new_comment.parent_comment = parent_comment

            new_comment.save()
            form = CommentForm()
    else:
        form = CommentForm()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # handle comments without full refresh
        context = {'comments': comments, 'post': post, "form": form}
        comments_html = 'portfolio/comments/comment_list.html'
        return JsonResponse({'html': render_to_string(comments_html, context, request=request)})

    context = {'post': post, 'comments': comments, 
            'form': form, 'user': user, " user_details":  user_details}
    return render(request, 'portfolio/post_detail.html', context)


def portfolio(request, username):
    # this class throws error if the user's userdetails query is empty
    """
    redirection method on login or signup containing portfolio
    """
    try:
        user = get_object_or_404(User, username=username)
    except User.DoesNotExist:
        user = None
    try:
        user_details = get_object_or_404(UserDetails, user=user)
    except UserDetails.DoesNotExist:
        user_details = None
    try:
        projects = Project.objects.filter(user=user).order_by("-created_at")
    except Project.DoesNotExist:
        projects = None
    try:
        posts = Post.objects.filter(user=user).order_by("-created_at")
    except Post.DoesNotExist:
        posts = None
    try:
        value = Skill.objects.filter(user=user)
        if value:
            skills =  value[0].name.split(", ")
        else:
            skills = None
    except Skill.DoesNotExist:
        skills = None
    context = {
        "user": request.user,
        "user_details": user_details,
        "projects": projects,
        "posts": posts,
        "skills": skills,
    }
    return render(request, "portfolio/portfolio.html", context)


@login_required
def portfolio_nav(request):
    """
    redirection method on login or signup containing portfolio
    """
    user = request.user
    user_details = get_object_or_404(UserDetails, user=user)
    context = {
        "user": user,
        "user_details": user_details,
    }
    return render(request, "portfolio_nav.html", context)


def main_nav(request):
    """
    redirection method on login or signup containing portfolio
    """
    user = request.user
    context = {
        "user": user,
    }
    return render(request, "base.html", context)
