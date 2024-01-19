from django.shortcuts import render, redirect
from django.http import HttpResponse ,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib import messages
from .forms import Comment_form
from .models import *
from django.core.mail import send_mail

def home(request):
   user = request.POST.get("name")
   context = {'user': request.user}
   return render(request , 'home.html',context)

def Blogs(request):
   return render(request , 'Blogs.html')

def About(request):
   return render(request , 'About.html')

def contact(request):
   if request.method == 'POST':
      con_name = request.POST.get('Name')
      con_email = request.POST.get('Email_addr')
      con_msg = request.POST.get('msg')

      # This is according to django email sending formate
      send_mail(
         'Message from' + con_name, # Name of email sender
         con_msg, # the mesage body here
         con_email, # Sender email
         ['Umairawan03125@gmail.com'],# Reciever Email
      )

      context = {'con_name': con_name}
      return render(request ,'contact.html' , context)
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
   


def DeleteComment(request ,pk ):
   comment_d = Comments.objects.filter(id = pk).first()
   print('req user: ', request.user, type(request.user))
   print('comment creator: ', comment_d.name, type(comment_d.name))
   
   if request.user.is_authenticated and request.user.username == comment_d.name:
      comment_d.delete()
      referer = request.META.get('HTTP_REFERER')
      if referer:
         return redirect(referer)
   else:
      return HttpResponse("You can't delete this comment")
   
   

