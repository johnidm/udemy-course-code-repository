from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    image_url = models.URLField(default='https://source.unsplash.com/random/800x400?writing,blog')
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='posts'
    )
    tags = models.ManyToManyField(Tag, related_name='posts')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(validators=[MinLengthValidator(10)])
    date = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.user_name} on {self.post.title}"
