import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
#el import de auth es para contar con los metodos de inicio de sesion y cerras sesion
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import CreatePostForm, UserForm, UserProfileForm, CommentForm


def index(request):
    blog = Post.objects.all()
    #blog = Post.objects.all().order_by('-fecha')[:5], para ordenar los recientes 5 :D
    query = request.GET.get('query')
    if query:
        blog = blog.filter(title__contains=query)

    return render(request, 'blog/index.html', {'contenido': blog})


def view_post(request, **kwargs):
    pk = kwargs.get('pk')
    post = Post.objects.get(pk=pk)

    #hago un llamado a todos los comentarios que pertenescan a este post
    comenta = Comment.objects.filter(post=post)

    #aca hago la insercion de comentarios,
    #tengo que hacerlo en la view_post ya que tengo el id
    #del post que es lo mas importante
    if request.method == 'POST':
        comentario = CommentForm(request.POST)

        if comentario.is_valid():
            coment = comentario.save(commit=False)
            coment.post = post
            coment.user = request.user.userprofile
            coment.save()
    else:
        comentario = CommentForm()
    return render(request, 'blog/view_post.html', {'post': post, 'form': comentario, 'comentari': comenta})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)

        if form.is_valid():
            foma = form.save(commit=False)
            foma.user = request.user.userprofile
            foma.fecha = datetime.datetime.now()
            foma.save()

            return redirect('/blog/')
    else:
        form = CreatePostForm
    return render(request, 'blog/add_post.html', {'form': form})


@login_required
def edit_post(request, **kwargs):
    pk = kwargs.get('pk')
    user = request.user.userprofile
    post = Post.objects.get(pk=pk)
    #este primer if es para verificar que solo el dueño del post puede editarlo
    if post.user == user:

        if request.method == 'POST':
            form = CreatePostForm(request.POST, instance=post)
            #el instance en esta linea es para mandar el id del post a editar

            if form.is_valid():
                form.save()
                #form = CreatePostForm()
                return redirect('/blog/')
        else:
            #poner esto aca
            form = CreatePostForm(instance=post)
    else:
        #aca le pongo al form none decirlee que no le mando nada para validar en la vista
        form = None
    return render(request, 'blog/edit.html', {'form': form, 'post': post})


@login_required
def delete_post(request, **kwargs):
    pk = kwargs.get('pk')
    user = request.user.userprofile
    post = Post.objects.get(pk=pk)
    if post.user == user:

        if request.method == 'POST':
            post.delete()
            return redirect('/blog/')
    else:
        post = None
    return render(request, 'blog/delete.html', {'post': post})


@login_required
def mis_post(request):
    query = request.GET.get('query')
    yo = request.user.userprofile
    mypost = Post.objects.filter(user=yo)
    if query:
        mypost = mypost.filter(title__contains=query)
    return render(request, 'blog/my_pos.html', {'mypost': mypost})


def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_pro = UserProfileForm(data=request.POST)

        if user_form.is_valid() and user_pro.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = user_pro.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print("hay error")

    else:
        user_form = UserForm()
        user_pro = UserProfileForm()
    return render(request, 'blog/registro.html', {'user': user_form, 'profile': user_pro,
                'registrado': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:
                login(request, user)
                return redirect('/blog/')
            else:
                return HttpResponse("no estas activa")

        else:
            print("problemas")
    else:
        pass
    return render(request, 'blog/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return redirect("/blog/login")
