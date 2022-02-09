from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns=[

    path('register',views.register, name='register'),
    path('login', views.login, name='login'),
    path ('logout/', views.logoutUser, name='logout'),
    # path('login', views.logout, name='logout'),

    path('index', views.index, name='index'),
    path('post', views.post, name='post'),
    path('post/<str:post_id>/', views.postDetail, name='postDetail'),
    path('postCreate', views.postCreate, name='postCreate'),
    path('updatePost/<str:pk>/', views.updatePost, name="updatePost"),
    path('deletePost/<str:pk>/', views.deletePost, name="deletePost"),
    path('category/', views.category, name="category"),
    
    
]