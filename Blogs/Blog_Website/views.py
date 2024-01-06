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
    if request.method == 'POST':
       cmt_form = request.POST.get('comment')
       cmt_user = request.user
       cmt_post = Post.objects.filter(id = pk).first()

       #print(cmt_form , cmt_user , cmt_post)
       new_cmt = Comments(post=cmt_post , cmt=cmt_form , name=cmt_user)
       print(cmt_form , cmt_user , cmt_post)
       new_cmt.save()
       return redirect('desc' , pk=pk) #We could work without it it will render 
         # desc page regardless we use redirect or not but upon reloading page
         # it will create another instance of the csame comment and display it
         # to tackle that I redirected to same page after saving comment. 
    
    post = Post.objects.filter(id = pk).first()
    comments= Comments.objects.filter(post=post)
    context = {'post': post , 'comments': comments}
    return render(request, 'detail.html', context)

    

def Search(request):
   if request.method == 'POST':
      s_blog = request.POST.get('sp')
      # print(s_blog) --for checking purposes
      search_b = Post.objects.filter(title__contains = s_blog)
      context = {'s_blog': s_blog , 'search_b':search_b}
      return render(request , 'search_result.html' , context)
   else:
      return render(request , 'search_result.html')

