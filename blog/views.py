from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post, Comment
from django.contrib.auth.decorators import permission_required

def is_in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


# Create your views here.
def blog_posts(request):
    posts = Post.objects.filter(published_date__lte = timezone.now())
    return render(request, "blog/blog_posts.html", {'posts': posts})



def read_post(request, id):
    post = Post.objects.get(pk=id)
    post.views += 1
    post.save()
    


    return render(request, "blog/read_post.html", 
        {
            'post': post, 
           
                  })


def comment(request, id):
    comment = Comment()
    comment.content = request.POST['comment']
    comment.post_id = id
    comment.author = request.user
    comment.save()
    return redirect(read_post, id)




