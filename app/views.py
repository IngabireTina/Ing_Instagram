from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def home(request):
    posts = Post.objects.all()
    users = User.objects.exclude(id=request.user.id)
    form = PostForm(request.POST or None, files=request.FILES)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user.Profile
        post.save()
        return redirect('home')
    context = {
        'posts': posts,
        'form': form,
        'users':users,
    }
    return render(request, 'home.html', context)
      
