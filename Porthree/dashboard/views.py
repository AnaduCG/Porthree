from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import UserDetailsForm, ProjectForm, SkillForm, PostForm
from MainApp.models import UserDetails, Project, Skill, Post


@login_required
def user_details_form(request):
    user = request.user

    try:
        # Check if data already exists for the current user
        user_details = UserDetails.objects.get(user=user)
    except UserDetails.DoesNotExist:
        user_details = None

    if request.method == "POST":
        form = UserDetailsForm(request.POST, request.FILES, instance=user_details)
        if form.is_valid():
            user_details = form.save(commit=False)
            user_details.user = request.user
            user_details.save()
            user.email = user_details.email
            user.save() # update user instance email
            return redirect('user-details')
    else:
        email = user.email if user.email != "" else user_details.email
        form = UserDetailsForm(instance=user_details, initial={'email': email})
    context = {
        "form": form,
        "user_details": user_details,
    }

    return render(request, "dashboard/user-details.html", context)



@login_required
def create_skill(request):
    user = request.user

    try:
        # Check if data already exists for the current user
        user_skills = Skill.objects.get(user=user)
    except Skill.DoesNotExist:
        user_skills = None
    try:
        # Check if data already exists for the current user
        user_details = UserDetails.objects.get(user=user)
    except UserDetails.DoesNotExist:
        user_details = None

    if request.method == "POST":
        form = SkillForm(request.POST, instance=user_skills)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user  # associate user
            skill.save()
            return redirect("create-skills")  # Redirect to a success page
    else:
        form = SkillForm(instance=user_skills)

    context = {
        "form": form,
        "user_skills": user_skills,
        "user_details": user_details,
    }

    return render(request, "dashboard/create-skills.html", context)


@login_required
def create_project(request, project_id=None):
    user = request.user
    try:
        # Check if data already exists for the current user
        user_details = UserDetails.objects.get(user=user)
    except UserDetails.DoesNotExist:
        user_details = None

    # Handling project deletion
    if request.method == "POST" and "delete_project" in request.POST:
        project_id_to_delete = request.POST.get("delete_project")
        project_to_delete = get_object_or_404(
            Project, id=project_id_to_delete, user=user
        )
        project_to_delete.delete()
        return redirect("create-project")  # Redirect to current page with deletion

    if project_id:
        # Editing an existing project
        project = get_object_or_404(Project, id=project_id, user=user)

        if request.method == "POST":
            form = ProjectForm(request.POST, request.FILES, instance=project)
            if form.is_valid():
                project = form.save(commit=False)
                project.user = request.user
                project.save()
                return redirect(
                    "create-project"
                )  # Redirect to page containing list and form
        else:
            form = ProjectForm(instance=project)

    else:
        # Creating a new project
        project = Project(user=user)

        if request.method == "POST":
            form = ProjectForm(request.POST, request.FILES, instance=project)
            if form.is_valid():
                project = form.save(commit=False)
                project.user = request.user
                project.save()
                return redirect("create-project")  # Redirect to project
        else:
            form = ProjectForm()

    projects_list = Project.objects.filter(user=user).order_by("-created_at")  # Retrieve all projects for display

    paginator = Paginator(projects_list, 7)
    page_number = request.GET.get("page")
    projects = paginator.get_page(page_number)
    project_count = projects_list.count()
    context = {
        "form": form,
        "projects": projects,
        "user_details": user_details,
        "project_count": project_count,
        }
    return render(request, "dashboard/create-project.html", context)

@login_required
def create_post(request, post_id=None):
    user = request.user
    try:
        # Check if data already exists for the current user
        user_details = UserDetails.objects.get(user=user)
    except UserDetails.DoesNotExist:
        user_details = None

    # Handling post deletion
    if request.method == "POST" and "delete_post" in request.POST:
        post_id_to_delete = request.POST.get("delete_post")
        post_to_delete = get_object_or_404(Post, id=post_id_to_delete, user=user)
        post_to_delete.delete()
        return redirect("create-post")  # Redirect to current page with deletion

    if post_id:
        # Editing an existing post
        post = get_object_or_404(Post, id=post_id, user=user)

        if request.method == "POST":
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                return redirect("create-post")  # Redirect to page containing list and form
        else:
            form = PostForm(instance=post)

    else:
        # Creating a new post
        post = Post(user=user)

        if request.method == "POST":
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                return redirect("create-post")  # Redirect to post
        else:
            form = PostForm()

    posts_list = Post.objects.filter(user=user).order_by("-created_at")  # Retrieve all posts for display

    paginator = Paginator(posts_list, 7)
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)
    post_count = posts_list.count()
    context = {
        "form": form,
        "posts": posts,
        "user_details": user_details,
        "post_count": post_count,
        }
    return render(request, "dashboard/create-post.html", context)
