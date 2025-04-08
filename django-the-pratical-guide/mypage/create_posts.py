from blog.models import Author, Post, Tag
from django.utils.text import slugify

# Create author if not exists
author, created = Author.objects.get_or_create(
    first_name='John',
    last_name='Doe',
    email='john.doe@example.com',
    bio='A passionate writer and tech enthusiast.'
)

# Create two blog posts
post1 = Post.objects.create(
    title='The Art of Python Programming',
    excerpt='Discover the beauty and power of Python programming language',
    content='Python is one of the most versatile programming languages. It offers great readability and extensive libraries that make development a joy. In this post, we explore the fundamentals and best practices of Python programming.',
    slug=slugify('The Art of Python Programming'),
    author=author
)

post2 = Post.objects.create(
    title='Django Web Development Tips',
    excerpt='Essential tips for building robust web applications with Django',
    content='Django is a high-level Python web framework that enables rapid development of secure and maintainable websites. Here are some essential tips and tricks for Django development that every developer should know.',
    slug=slugify('Django Web Development Tips'),
    author=author
)

print('Created posts:', post1.title, 'and', post2.title)
