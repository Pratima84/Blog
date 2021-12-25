from django import http
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .forms import PostForm
from .models import Post





def index(request):
    posts= Post.objects.all
    context= {'posts':posts} 
    return render(request,'base/index.html',context)
   
  
   
    
def post(request):
     return render(request,'base/post.html')
    

def postDetail(request,post_id):
    postDetail = get_object_or_404(Post, pk=post_id) #pass this veriable to template to render value
    context= {'postDetail':postDetail}  #{'call from loop': call from the function}
    print(postDetail)
    return render(request,'base/post.html',context)


def postCreate(request):
    if request.method == "Post":
        form= PostForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('index.html')

            except:
                pass
        else:
            form = PostForm()
        return render(request,'index.html',{'form':form})



        