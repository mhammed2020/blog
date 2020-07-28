from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages

from django.core.paginator import Paginator

# Create your views here.

def allPosts(request):
    posts = Post.objects.all()

    ##pagination
    posts = Post.objects.all()

    paginator = Paginator(posts, 3)  # Show 25 contacts per page.

    page = request.GET.get('page')
    posts = paginator.get_page(page)

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




def create_post(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            new_form=form.save(commit=False)
            new_form.user=request.user
            new_form.save()
            messages.success(request, 'Post created successfully')
            return redirect('/')

    else:
        form = PostForm()

    context={

        'form':form,
    }
    return  render(request,'Post/create.html',context)

def editPost(request,id):
    detailPost=get_object_or_404(Post,id=id)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=detailPost)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('/')
    else:
        form = PostForm(instance=detailPost)

    context = {

        'form': form,
    }
    return render(request,'Post/edit.html', context)
