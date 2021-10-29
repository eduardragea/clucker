from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .forms import LogInForm, SignUpForm, PostForm
from .models import User

def feed(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid() :
            post = form.save()
    form = PostForm()
    return render(request, 'feed.html', {'form': form})

def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        user = request.User
        form.author = user
        if form.is_valid():
            if user.is_authenticated:
                post = form.save()
                return redirect('feed')
    else:
        form = PostForm()
    return render(request, 'feed.html', {'form': form})

def log_in(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('feed')
        messages.add_message(request, messages.ERROR, "The credentials provided were invalid!")
    form = LogInForm()
    return render(request, 'log_in.html', {'form': form})

def log_out(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'home.html')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('feed')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})

def user_list(request):
    user_list = User.objects.all()
    return render(request, 'user_list.html', {'user_list': user_list})

def show_user(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'show_user.html', {'user': user})
