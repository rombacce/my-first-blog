from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
<<<<<<< HEAD
#
=======

def post_list(request):
    name = "Celina" 
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'name': name})
>>>>>>> 06c8f8903b487def7eff676689ac05c80f8d08cd
