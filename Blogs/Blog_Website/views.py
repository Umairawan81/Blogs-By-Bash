from django.shortcuts import render, redirect
from django.http import HttpResponse ,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .forms import Comment_form
from .models import *

def home(request):
   user = request.POST.get("name")
   context = {'user': request.user}
   return render(request , 'home.html',context)

def Blogs(request):
   return render(request , 'Blogs.html')

def About(request):
   return render(request , 'About.html')

def contact(request):
   return render(request , 'contact.html')


def blogView(request ):
    context ={}
    context["dataset"] = Post.objects.all()
    return render(request, 'Blogs.html', context)


def DescView(request, pk):
    post = Post.objects.filter(id = pk).first()
    comments= Comments.objects.filter(post=post)
    context = {'post': post , 'comments': comments}
    return render(request, 'detail.html', context)


def AddComment(request, pk):
   return render(request , 'add_cmt.html')

    
def postComment(request):
   # Form creation krni ha abhi.
   if request.method == 'POST':
      cmt_post = Comment_form(request.POST)
      if cmt_post.is_valid():
         cleaned_data = cmt_post.cleaned_data
         print(cleaned_data)
         cmt_post.save()
      
   return HttpResponseRedirect(request.META.get('HTTP_REFERER'), {'cmt_post': cmt_post})



