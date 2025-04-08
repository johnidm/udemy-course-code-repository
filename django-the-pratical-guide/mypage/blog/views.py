from django.shortcuts import render

all_posts = [
    {
        "title": "First Post",
        "excerpt": "This is the first post's excerpt...",
        "content": """
        This is the full content of the first post. It contains multiple paragraphs and can be quite long.

        You can include formatting, code examples, and other content here. This is where the main body of your blog post goes.

        Feel free to write as much as you need in this section.
        """,
        "date": "2025-04-01",
        "slug": "first-post",
        "image": "https://fastly.picsum.photos/id/11/2500/1667.jpg?hmac=xxjFJtAPgshYkysU_aqx2sZir-kIOjNR9vx0te7GycQ"
    },
    {
        "title": "Second Post",
        "excerpt": "This is the second post's excerpt...",
        "content": """
        Welcome to the second post! This is another example of a full blog post content.

        You can write about different topics, include images, and format your text however you like.

        This is just dummy content for now, but it shows how the layout will look with real content.
        """,
        "date": "2025-04-01",
        "slug": "second-post",
        "image": "https://fastly.picsum.photos/id/7/4728/3168.jpg?hmac=c5B5tfYFM9blHHMhuu4UKmhnbZoJqrzNOP9xjkV4w3o"
    }
]

def index(request):
    return render(request, "blog/index.html")

def posts(request):
    return render(request, "blog/posts.html", {"posts": all_posts})

def post_detail(request, slug):
    # Find the post that matches the slug
    post = next((post for post in all_posts if post["slug"] == slug), None)
    return render(request, "blog/post_detail.html", {"post": post})
