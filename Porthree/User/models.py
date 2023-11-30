from uuid import uuid4
from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.

class User(models.Model):
    """
    This model represents a user in the database
    and user associated data
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(unique=True)
    career_title = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(5)])
    password = models.CharField(max_length=255)
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.user_name

class PostTags(models.Model):
    """
    This model represents the tags for each post
    It has a many to many relationship
    with posts
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    """
    this model holds data associated with a specific
    post
    Note: Many to many relationship exists between
    tag and post
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    tags = models.ManyToManyField(PostTags, related_name='posts')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    like = models.BooleanField(default=False)
    shared = models.BooleanField(default=False)

    def get_post(self):
        return "\n".join([i.post for i in self.post.all()])

    def __str__(self):
        return self.title

class Comment(models.Model):
    """
    This model handles comments per post
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    like = models.BooleanField(default=False)

    def __str__(self):
        return f"Comment by {self.post.user.username} on post '{self.post.title}'"

class Skill(models.Model):
    """
    This models lists all the skills of a specific user
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Social(models.Model):
    """
    This model contains the social media links
    for a particular user
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    icon = models.FileField(upload_to='icons/')
    name = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.name

class Hero(models.Model):
    """
    This model defines the data for the hero section
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    intro = models.TextField()

    def __str__(self):
        return f"Hero headline: {self.headline} for {self.user}"

class Theme(models.Model):
    """
    This model defines the theme of a specific user
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    primary_color = models.CharField(max_length=255)
    secondary_color = models.CharField(max_length=255)

    def __str__(self):
        return f"Theme for {self.user}"

class Project(models.Model):
    """
    This model describes the programmers projects
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    about = models.TextField()
    comment = models.TextField()
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(5)])

    def __str__(self):
        return f"Project by {self.user}"

class ProjectTools(models.Model):
    """
    this model defines the tools used for a
    specific project
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"Tool '{self.name}' for project by {self.user}"