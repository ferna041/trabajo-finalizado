from django.shortcuts import redirect, render, get_object_or_404
from .models import Post
from green.form import PostForm , SocialCommentForm


def home(request):
    data = Post.objects.all()
    return render(request, "home.html", {"posts": data})








#primero basico
def m1(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/primero_basico/Matematicas.html", {"posts": data})
def l1(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/primero_basico/Lenguaje.html", {"posts": data})
def c1(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/primero_basico/ciencias.html", {"posts": data})
def h1(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/primero_basico/Historia.html", {"posts": data})
def i1(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/primero_basico/ingles.html", {"posts": data})
def o1(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/primero_basico/otros.html", {"posts": data})


#segundo basico


def m2(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/segundo basico/Matematicas.html", {"posts": data})
def l2(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/segundo basico/Lenguaje.html", {"posts": data})
def c2(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/segundo basico/ciencias.html", {"posts": data})
def h2(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/segundo basico/Historia.html", {"posts": data})
def i2(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/segundo basico/ingles.html", {"posts": data})
def o2(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/segundo basico/otros.html", {"posts": data})
#tercero basico


def m3(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/tercero basico/Matematicas.html", {"posts": data})
def l3(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/tercero basico/Lenguaje.html", {"posts": data})
def c3(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/tercero basico/ciencias.html", {"posts": data})
def h3(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/tercero basico/Historia.html", {"posts": data})
def i3(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/tercero basico/ingles.html", {"posts": data})
def o3(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/tercero basico/otros.html", {"posts": data})

#cuarto basico

def m4(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/cuarto basico/Matematicas.html", {"posts": data})
def l4(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/cuarto basico/Lenguaje.html", {"posts": data})
def c4(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/cuarto basico/ciencias.html", {"posts": data})
def h4(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/cuarto basico/Historia.html", {"posts": data})
def i4(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/cuarto basico/ingles.html", {"posts": data})
def o4(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/cuarto basico/otros.html", {"posts": data})

#cuarto basico

def m5(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/quinto basico/Matematicas.html", {"posts": data})
def l5(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/quinto basico/Lenguaje.html", {"posts": data})
def c5(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/quinto basico/ciencias.html", {"posts": data})
def h5(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/quinto basico/Historia.html", {"posts": data})
def i5(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/quinto basico/ingles.html", {"posts": data})
def o5(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/quinto basico/otros.html", {"posts": data})

#sexto basico

def m6(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/sexto basico/Matematicas.html", {"posts": data})
def l6(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/sexto basico/Lenguaje.html", {"posts": data})
def c6(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/sexto basico/ciencias.html", {"posts": data})
def h6(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/sexto basico/Historia.html", {"posts": data})
def i6(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/sexto basico/ingles.html", {"posts": data})
def o6(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/sexto basico/otros.html", {"posts": data})

#septimo basico

def m7(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/septimo basico/Matematicas.html", {"posts": data})
def l7(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/septimo basico/Lenguaje.html", {"posts": data})
def c7(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/septimo basico/ciencias.html", {"posts": data})
def h7(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/septimo basico/Historia.html", {"posts": data})
def i7(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/septimo basico/ingles.html", {"posts": data})
def o7(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/septimo basico/otros.html", {"posts": data})

#octavo basico

def m8(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/octavo basico/Matematicas.html", {"posts": data})
def l8(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/octavo basico/Lenguaje.html", {"posts": data})
def c8(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/octavo basico/ciencias.html", {"posts": data})
def h8(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/octavo basico/Historia.html", {"posts": data})
def i8(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/octavo basico/ingles.html", {"posts": data})
def o8(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/octavo basico/otros.html", {"posts": data})

#1ro
def bI(request):
    data = Post.objects.all()
    return render(request, "grados/media/primero_medio/biologia.html", {"posts": data})
def fI(request):
    data = Post.objects.all()
    return render(request, "grados/media/primero_medio/fisica.html", {"posts": data})
def hI(request):
    data = Post.objects.all()
    return render(request, "grados/media/primero_medio/Historia.html", {"posts": data})
def iI(request):
    data = Post.objects.all()
    return render(request, "grados/media/primero_medio/Ingles.html", {"posts": data})
def lI(request):
    data = Post.objects.all()
    return render(request, "grados/media/primero_medio/Lenguaje.html", {"posts": data})
def mI(request):
    data = Post.objects.all()
    return render(request, "grados/media/primero_medio/Matematicas.html", {"posts": data})
def oI(request):
    data = Post.objects.all()
    return render(request, "grados/media/primero_medio/otros.html", {"posts": data})
def qI(request):
    data = Post.objects.all()
    return render(request, "grados/media/primero_medio/quimica.html", {"posts": data})


#2do
def bII(request):
    data = Post.objects.all()
    return render(request, "grados/media/segundo_medio/biologia.html", {"posts": data})
def fII(request):
    data = Post.objects.all()
    return render(request, "grados/media/segundo_medio/fisica.html", {"posts": data})
def hII(request):
    data = Post.objects.all()
    return render(request, "grados/media/segundo_medio/Historia.html", {"posts": data})
def iII(request):
    data = Post.objects.all()
    return render(request, "grados/media/segundo_medio/Ingles.html", {"posts": data})
def lII(request):
    data = Post.objects.all()
    return render(request, "grados/media/segundo_medio/Lenguaje.html", {"posts": data})
def mII(request):
    data = Post.objects.all()
    return render(request, "grados/media/segundo_medio/Matematicas.html", {"posts": data})
def oII(request):
    data = Post.objects.all()
    return render(request, "grados/media/segundo_medio/otros.html", {"posts": data})
def qII(request):
    data = Post.objects.all()
    return render(request, "grados/media/segundo_medio/quimica.html", {"posts": data})

#3r
def bIII(request):
    data = Post.objects.all()
    return render(request, "grados/media/tercero_medio/biologia.html", {"posts": data})
def fIII(request):
    data = Post.objects.all()
    return render(request, "grados/media/tercero_medio/fisica.html", {"posts": data})
def hIII(request):
    data = Post.objects.all()
    return render(request, "grados/media/tercero_medio/Historia.html", {"posts": data})
def iIII(request):
    data = Post.objects.all()
    return render(request, "grados/media/tercero_medio/Ingles.html", {"posts": data})
def lIII(request):
    data = Post.objects.all()
    return render(request, "grados/media/tercero_medio/Lenguaje.html", {"posts": data})
def mIII(request):
    data = Post.objects.all()
    return render(request, "grados/media/tercero_medio/Matematicas.html", {"posts": data})
def oIII(request):
    data = Post.objects.all()
    return render(request, "grados/media/tercero_medio/otros.html", {"posts": data})
def qIII(request):
    data = Post.objects.all()
    return render(request, "grados/media/tercero_medio/quimica.html", {"posts": data})
def qaIII(request):
    data = Post.objects.all()
    return render(request, "grados/media/tercero_medio/quimica_adv.html", {"posts": data})
def baIII(request):
    data = Post.objects.all()
    return render(request, "grados/media/tercero_medio/biologia_adv.html", {"posts": data})
def faIII(request):
    data = Post.objects.all()
    return render(request, "grados/media/tercero_medio/fisica_adv.html", {"posts": data})
def maIII(request):
    data = Post.objects.all()
    return render(request, "grados/media/tercero_medio/Mat_adv.html", {"posts": data})

#4to
def bIV(request):
    data = Post.objects.all()
    return render(request, "grados/media/cuarto_medio/biologia.html", {"posts": data})
def fIV(request):
    data = Post.objects.all()
    return render(request, "grados/media/cuarto_medio/fisica.html", {"posts": data})
def hIV(request):
    data = Post.objects.all()
    return render(request, "grados/media/cuarto_medio/Historia.html", {"posts": data})
def iIV(request):
    data = Post.objects.all()
    return render(request, "grados/media/cuarto_medio/Ingles.html", {"posts": data})
def lIV(request):
    data = Post.objects.all()
    return render(request, "grados/media/cuarto_medio/Lenguaje.html", {"posts": data})
def mIV(request):
    data = Post.objects.all()
    return render(request, "grados/media/cuarto_medio/Matematicas.html", {"posts": data})
def oIV(request):
    data = Post.objects.all()
    return render(request, "grados/media/cuarto_medio/otros.html", {"posts": data})
def qIV(request):
    data = Post.objects.all()
    return render(request, "grados/media/cuarto_medio/quimica.html", {"posts": data})
def qaIV(request):
    data = Post.objects.all()
    return render(request, "grados/media/cuarto_medio/quimica_adv.html", {"posts": data})
def baIV(request):
    data = Post.objects.all()
    return render(request, "grados/media/cuarto_medio/biologia_adv.html", {"posts": data})
def faIV(request):
    data = Post.objects.all()
    return render(request, "grados/media/cuarto_medio/fisica_adv.html", {"posts": data})
def maIV(request):
    data = Post.objects.all()
    return render(request, "grados/media/cuarto_medio/Mat_adv.html", {"posts": data})


#PDT
def b(request):
    data = Post.objects.all()
    return render(request, "grados/media/PDT/biologia.html", {"posts": data})
def f(request):
    data = Post.objects.all()
    return render(request, "grados/media/PDT/fisica.html", {"posts": data})
def h(request):
    data = Post.objects.all()
    return render(request, "grados/media/PDT/Historia.html", {"posts": data})
def i(request):
    data = Post.objects.all()
    return render(request, "grados/media/PDT/Ingles.html", {"posts": data})
def l(request):
    data = Post.objects.all()
    return render(request, "grados/media/PDT/Lenguaje.html", {"posts": data})
def m(request):
    data = Post.objects.all()
    return render(request, "grados/media/PDT/Matematicas.html", {"posts": data})
def o(request):
    data = Post.objects.all()
    return render(request, "grados/media/PDT/otros.html", {"posts": data})
def q(request):
    data = Post.objects.all()
    return render(request, "grados/media/PDT/quimica.html", {"posts": data})
def qa(request):
    data = Post.objects.all()
    return render(request, "grados/media/PDT/quimica_adv.html", {"posts": data})
def ba(request):
    data = Post.objects.all()
    return render(request, "grados/media/PDT/biologia_adv.html", {"posts": data})
def fa(request):
    data = Post.objects.all()
    return render(request, "grados/media/PDT/fisica_adv.html", {"posts": data})
def ma(request):
    data = Post.objects.all()
    return render(request, "grados/media/PDT/Mat_adv.html", {"posts": data})

from users import models
from users import views
from users import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.models import User


from django.contrib.auth.decorators import login_required



@login_required(login_url='green:home.html')
def create_post(request):
    
    if request.user.is_authenticated:
         current_user = request.user
     
    
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post =form.save(commit=False)
            post.author = current_user
            post.save()
            return redirect('green:home.html')
    return render(request, 'post/posteos.html', {"form": form})


from django.views import View

def Comment(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = SocialCommentForm()

        context = {
            'post': post,
            'form': form,
        }

        return render(request, 'post_detail.html', context)

   

