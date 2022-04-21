from django.views.decorators.http import require_http_methods,require_POST, require_safe
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Anonymous,  Comment
from .forms import AnonymousForm, CommentForm

# Create your views here.
@require_safe
def index(request):
    anonymouses = Anonymous.objects.order_by('-created_at')[:20]
    context = {
        'anonymouses': anonymouses,
    }    
    return render(request, 'anonymous/index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == "POST":
        form = AnonymousForm(request.POST)
        if form.is_valid():
            anonymous = form.save(commit=False)
            anonymous.user = request.user
            anonymous.save()
            return redirect('anonymous:detail', anonymous.pk)

    else:
        form = AnonymousForm()

    context = {
        'form': form,
    }
    return render(request, 'anonymous/create.html', context)


@require_safe
def detail(request, pk):
    anonymouses = Anonymous.objects.order_by('-created_at')[:10]
    anonymous = get_object_or_404(Anonymous, pk=pk)
    comments = anonymous.comment_set.all()
    anonymous.view_cnt += 1
    anonymous.save()
    comment_form = CommentForm

    context = {
        'anonymouses' : anonymouses,
        'anonymous': anonymous,
        'comments' : comments,
        'comment_form' : comment_form,
    }
    return render(request, 'anonymous/detail.html', context)

@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        anonymous = get_object_or_404(Anonymous, pk=pk)
        if request.user == anonymous.user:
            anonymous.delete()
    return redirect('anonymous:index')

@require_POST
def create_comment(request, pk):
    if request.user.is_authenticated:
        anonymous = get_object_or_404(Anonymous, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.anonymous = anonymous
            comment.user = request.user
            comment.save()
            anonymous.save()
        print(comment_form.errors)
        return redirect('anonymous:detail', anonymous.pk)
        
    return redirect('accounts:login')

@require_POST
def delete_comment(request, pk, comment_pk):
    if request.user.is_authenticated:
        anonymous = get_object_or_404(Anonymous, pk=pk)
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('anonymous:detail', anonymous.pk)


@require_POST
def like_article(request, pk):
    if request.user.is_authenticated:
        anonymous = get_object_or_404(Anonymous, pk = pk)
        if anonymous.like_users.filter(pk = request.user.pk).exists():
            anonymous.like_users.remove(request.user)
        else:
            anonymous.like_users.add(request.user)
    return redirect('anonymous:detail', anonymous.pk)