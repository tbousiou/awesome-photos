from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Post, Tag
from .forms import PostForm, PostEditForm
import requests
from bs4 import BeautifulSoup
# Create your views here.

def home_view(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()
    return render(request, 'home.html', {'posts': posts, 'tags': tags})

def post_create_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            website = requests.get(form.data['source_url'])
            sourcecode = BeautifulSoup(website.text, 'html.parser')
            find_image = sourcecode.select('meta[content^="https://live.staticflickr.com/"]')
            try:   
                image = find_image[0]['content']
            except:
                messages.error(request, 'Requested image is not on Flickr!')
                return redirect('post-create')
            
            post.image_url = image
            
            find_title = sourcecode.select('h1.photo-title')
            title = find_title[0].text.strip()
            post.title = title
            
            find_artist = sourcecode.select('a.owner-name')
            artist = find_artist[0].text.strip() 
            post.artist = artist
            
            # post.author = request.user

            post.save()
            # After you’ve manually saved the instance produced by the form,
            # you can invoke save_m2m() to save the many-to-many form data. 
            form.save_m2m()
            return redirect('home-page')
    
    form = PostForm()
    return render(request, 'post_create.html', {'form': form})


def post_delete_view(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('home-page')
    
    return render(request, 'post_delete.html', {'post': post})


def post_edit_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostEditForm(instance=post)

    if request.method == 'POST':
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated')
            return redirect('home-page')
    
    context = {
        'post' : post,
        'form' : form
    }
    return render(request, 'post_edit.html', context)

def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def tag_posts_view(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = tag.posts.all()
    tags = Tag.objects.all()
    return render(request, 'tag_posts.html', {'active_tag': tag, 'posts': posts, 'tags': tags})