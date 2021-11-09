from django.shortcuts import render

posts = [
    {
        "author": "Rijal Islami",
        "title": "Blog post 1",
        "content": "First post content",
        "date": "August 27, 2021"
    },
    {
        "author": "John Doe",
        "title": "Blog post 2",
        "content": "Second post content",
        "date": "August 28, 2021"
    }
]

def home(request):
    context = {
        "posts": posts
    }
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html")
