
from django import http
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .forms import PostForm
from .models import Category, Post





def index(request):
    categories= Category.objects.all
    posts= Post.objects.all
    context= {'posts':posts,'categories':categories} 
    return render(request,'base/index.html',context)
   
  
   
    
def post(request):
    posts= Post.objects.all
    context= {'posts':posts} 
    print(posts)
    return render(request,'base/post.html', context)
    

def postDetail(request,post_id):
    postDetail = get_object_or_404(Post, pk=post_id) #pass this veriable to template to render value
    context= {'postDetail':postDetail}  #{'call from loop': call from the function}
    print(postDetail)
    return render(request,'base/postDetail.html',context)


def postCreate(request):
    form = PostForm(request.POST) 
    if form.is_valid():  
        try:  
            form.save()  
            return redirect('/index')  
        except:  
                pass  
    else:  
        form = PostForm()  
        context= {'form':form, }

    return render(request,'base/postCreate.html', context)   

      
def updatePost(request,pk):

    posts= Post.objects.get(id=pk)
    form = PostForm(instance=posts)
    if request.method =='POST':
        form = PostForm(request.POST,instance=posts)
        if form.is_valid():  
            form.save()
            return redirect('index')
    context={'form': form,'posts':posts}
    # context={'form': form,'categories': catogeries,'post':post}
    return render(request,'base/updatePost.html',context)

def deletePost(request,pk):
    post= Post.objects.get(id=pk)
    if request.method== 'POST':
        post.delete()
        return redirect('index')
    return render(request,'base/delete.html',{'obj':post})

def category(request):
    categories= Category.objects.all
    print(category)
    context={'categories': categories}
    return render(request,'base/category.html', context)