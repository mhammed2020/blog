from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
# Create your views here.

def allPosts(request):
    posts = Post.objects.all()
    context= {
        'posts':posts,

    }
    return  render(request,'Post/allposts.html',context)


def detailPost(request,id):
    # detailPost = Post.objects.get(id = id)

    # productDetail = Product.objects.get(PRDSlug=slug)
    detailPost = get_object_or_404(Post, id=id)

    context= {
        'detailPost':detailPost,

    }
    return  render(request,'Post/jobDetail.html',context)