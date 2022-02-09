from turtle import title
from django.db.models import Q
from django.db.models.query import QuerySet
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import password_changed
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.template import context
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category, Post
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, login, logout


#funstion for user registration

def register(request):
    if request.method =="POST":
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account created successfully.")
            return redirect('login')
    else:
        form= UserCreationForm()
           
    return render(request,'base/register.html',  {'form':form})

#function for login user

def login(request):
    if request.method== 'POST':
        form = AuthenticationForm(request= request, data=request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username') #convert data to the appropriate type
            password= form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                auth_login(request,user)
                messages.info(request, "You are logged in Successfully")
                return redirect('/index')
            else:
                messages.error(request,"Invalid Username or Password")

        else:
            messages.error(request,"Invalid Username or Password")
    form = AuthenticationForm()
    context ={'form':form}
    return render(request,'base/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect(index)

#Render post detail to  index  
def index(request):
    q= request.GET.get('q') if request.GET.get('q') != None else ''

    posts= Post.objects.filter(
        Q(category__name__icontains=q ) |
        Q(title__icontains=q)|
        Q(content__icontains=q)
        )

    categories=Category.objects.all
    post_count = posts.count() 
    context= {'posts':posts,'categories':categories,'post_count':post_count} 
    return render(request,'base/index.html',context)
    
  
   
    
def post(request):
    posts= Post.objects.all
    context= {'posts':posts} 
    print(posts)
    return render(request,'base/post.html', context)
    

#Render post detail to template  
def postDetail(request,post_id):
    postDetail = get_object_or_404(Post, pk=post_id) #pass this veriable to template to render value
    context= {'postDetail':postDetail}  #{'call from loop': call from the function}
    print(postDetail)
    return render(request,'base/postDetail.html',context)


#Create post function  
@login_required(login_url = 'login')
def postCreate(request):
    form = PostForm()
    categories = Category.objects.all()
    if request.method == 'POST':
        category_name= request.POST.get('category') 
        category, created = Category.objects.get_or_create(name = category_name)
        Post.objects.create(
          
            category= category,
            title=request.POST.get('title'),
            content= request.POST.get('content'),
        )
        return redirect('index')
        
    context= {'form':form, 'categories':categories }
    return render(request,'base/postCreate.html', context)   


    # if form.is_valid():  
    #     try:  
    #         form.save()  
    #         return redirect('/index')  
    #     except:  
    #             pass  
    # else:  
    #     form = PostForm()  
    #     context= {'form':form, }

   

#Update post function       
def updatePost(request,pk):
    posts= Post.objects.get(id=pk)
    form = PostForm(instance=posts)
    if request.method =='POST':
        form = PostForm(request.POST,instance=posts)
        if form.is_valid():  
            form.save()
            return redirect('/index')
    context={'form': form,'posts':posts}
    # context={'form': form,'categories': catogeries,'post':post}
    return render(request,'base/updatePost.html',context)


#Delete post function  
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