
from sre_constants import SUCCESS
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView,DetailView,ListView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy



def home(request):
    return render(request, 'home.html')

class BlogPost(ListView):
    model=Post
    template_name='blogs.html'
    ordering=['-post_date']

class Post_View(DetailView):
    model=Post
    template_name='postview.html'

class CreatePost(CreateView):
    model= Post
    template_name='createpost.html'
    fields='__all__'
    
class DeletePost(DeleteView):
    model=Post
    template_name='deletepost.html'
    success_url=reverse_lazy('home')
    
class EditBlog(UpdateView):
    model=Post
    template_name='editpost.html'
    fields=['title','body']

def signup(request):
    return render(request, 'signup.html')

def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            return redirect('login')
        else:
            return redirect('home')

    else:
        return HttpResponse("404 Error!")


def loginpage(request):
    return render(request, 'login.html')

def handleLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('blog')
        else:
            return redirect('home')

    else:
        return HttpResponse("Error!")
    
def handleLogout(request):
    logout(request)
    return redirect('home')
    
