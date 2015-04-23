from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Post
from blog.forms import CreatePostForm, EditPostForm

def index(request):
    blog = Post.objects.all()
    query  = request.GET.get('query')
    if query:
        blog = blog.filter(title__contains=query)

    return render(request,'blog/index.html', {'contenido':blog})


def view_post(request, **kwargs):
    pk = kwargs.get('pk')
    post = Post.objects.get(pk=pk)

    return render(request, 'blog/view_post.html', {'post':post})


def create_post(request):

    if request.method == 'POST':
        form =CreatePostForm(request.POST)
        if form.is_valid():

            foma = form.save(commit=False)
            foma.user = request.user.userprofile
            foma.save()

            return redirect('/blog/')
    else:
        form = CreatePostForm
    return render(request, 'blog/add_post.html', {'form': form})


def edit_post(request, **kwargs):
    pk = kwargs.get('pk')

    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        form = CreatePostForm(request.POST, instance=post)#el instance en esta linea es para mandar el id del post a editar
        if form.is_valid():
            form.save()
            #form = CreatePostForm()
            return redirect('/blog/')

    else:
        form = CreatePostForm(instance=post)#poner esto aca 
    return render(request, 'blog/edit.html', {'form': form, 'post':post})


def delete_post(request,**kwargs):
    pk = kwargs.get('pk')

    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        post.delete()

        return redirect('/blog/')
    return render(request, 'blog/delete.html', {'post': post})



def mis_post(request):
    query = request.GET.get('query')
    yo = request.user.userprofile
    mypost = Post.objects.filter(user=yo)
    if query:
        mypost = mypost.filter(title__contains=query)
    return render(request, 'blog/my_pos.html', {'mypost': mypost})