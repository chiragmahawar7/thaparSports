from django.shortcuts import render

#from .models import Post


def home(request):
    # post = Post.objects.all().order_by('-timestamp')
    # context = {
    #     "post": post,
    # }
    return render(request, 'gallery/index.html')