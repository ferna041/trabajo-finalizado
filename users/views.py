from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from green.models import Post
from .forms import UserLoginForm, UserSignUpForm


def login_view(request):
    login_form = UserLoginForm(request.POST or None)
    if login_form.is_valid():
        email = login_form.cleaned_data.get('email')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Has iniciado sesion correctamente')
            return redirect('green:home.html')
        else:
            messages.warning(
                request, 'Correo Electronico o Contrasena invalida')
            return redirect('green:home.html')

    messages.error(request, 'Formulario Invalido')
    return redirect('green:home.html')


def signup_view(request):
    signup_form = UserSignUpForm(request.POST or None)
    if signup_form.is_valid():
        email = signup_form.cleaned_data.get('email')
        nombre = signup_form.cleaned_data.get('nombre')
        ciudad = signup_form.cleaned_data.get('ciudad')
        password = signup_form.cleaned_data.get('password')
        try:
            user = get_user_model().objects.create(
                email=email,
                nombre=nombre,
                ciudad=ciudad,
                password=make_password(password),
                is_active=True
            )
            login(request, user)
            return redirect('green:home.html')

        except Exception as e:
            print(e)
            return JsonResponse({'detail': f'{e}'})


def logout_view(request):
    logout(request)
    return redirect('green:home.html')


@login_required(login_url='green:home.html')
def profile_view(request):
    return render(request, 'users/profile.html')


def user_detail(request, slug):
    user = get_object_or_404(get_user_model(), slug=slug)
    is_follower = False
    try:
        if user.is_follower(request.user):
            is_follower = True
    except:
        messages.warning(
            request, 'Debes Iniciar sesion para mas funcionalidades')
        return redirect("green:home.html")

    return render(request, 'users/user_detail.html', {'user_detail': user, "is_follower": is_follower})


@login_required(login_url='green:home.html')
def follow(request, slug):
    to_follow = get_object_or_404(get_user_model(), slug=slug)
    if to_follow.is_follower(request.user):
        to_follow.followers.remove(request.user)
    else:
        to_follow.followers.add(request.user)
    to_follow.save
    return redirect(to_follow)





@login_required(login_url='users:profile.html')
def following_view(request):
    return render(request, 'users/seguidos_profile.html')


@login_required(login_url='users:profile.html')
def followers_view(request):
    if request.user.is_authenticated:
        user = request.user
        data = user.followers.all()
    return render(request, 'users/seguidores_profile.html')


@login_required(login_url='users:profile.html')
def followers_user_view(request):
    return render(request, 'users/seguidores_user.html')


@login_required(login_url='users:profile.html')
def following_user_view(request):
    return render(request, 'users/seguidos_user.html', { 'user_detail': user})



@login_required(login_url='green:home.html')
def post_profile(request):
    data = Post.objects.all()
    return render(request, "users/post_profile.html", {"posts": data})


@login_required(login_url='green:home.html')
def post_user(request):
    data = Post.objects.all()

    return render(request, "users/post_user.html", { "user_detail": user, "posts": data})





