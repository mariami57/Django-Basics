from datetime import datetime

from django.http.response import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return HttpResponse("Welcome to the forum app")

def dashboard(request):

    if request.method == "POST":
        return redirect('index')

    context = {
            "posts":
            [
                {
                    "title": "How to work with templates?",
                    "author": "Maria M",
                    "content": "Hey how can I work with templates in Django?",
                    "created_at": datetime.now(),
                },

                {
                    "title": "Was the lecture good",
                    "author": "",
                    "content": "Should I watch it?",
                    "created_at": datetime.now(),
                },

                {
                    "title": "What is the next lecture",
                    "author": "Maria M",
                    "content": "**hey** guys, I `have` no idea, pls answer!!!",
                    "created_at": datetime.now(),
                },
            ]

        }

    return render(request, "base.html", context)