from django.urls import path
from . import views
from .views import CreatePost, Post_View,BlogPost,EditBlog,DeletePost

urlpatterns = [
    path("", views.home, name="home"),
    path("blog",BlogPost.as_view(),name='blog'),
    path("signup", views.signup, name="signup"),
    path("login", views.loginpage, name="login"),
    path('handlesignup/', views.handleSignup, name='handleSignup'),
    path('handlelogin/', views.handleLogin, name='handleLogin'),
    path('handlelogout/', views.handleLogout, name='logout'),
    path("createpost/", CreatePost.as_view(), name='createpost'),
    path('postview/ <int:pk>',Post_View.as_view(),name='postview'),
    path('post/edit/<int:pk>',EditBlog.as_view(),name='editpost'),
    path('post/delete/<int:pk>',DeletePost.as_view(),name='deletepost')
]

