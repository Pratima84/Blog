from django.urls import path
from . import views


urlpatterns=[

    path('', views.index, name='index'),
    path('post', views.post, name='post'),
    path('post/<str:post_id>/', views.postDetail, name='postDetail'),
    path('base/post_form',views.postCreate, name='postCreate')
    
]

