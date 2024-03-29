from django.shortcuts import render, redirect
from django.http import HttpResponse ,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib import messages
from .forms import Comment_form
from .models import *
from django.core.mail import send_mail
from django.contrib.auth import authenticate , login ,logout

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
      
   if request.user.is_authenticated and request.user.username == comment_d.name:
      print('req user: ', request.user, type(request.user))
      print('comment creator: ', comment_d.name, type(comment_d.name))
      comment_d.delete()
      referer = request.META.get('HTTP_REFERER')
      if referer:
         return redirect(referer)
   else:
       return HttpResponse("Only comment's creator can delete!")
   
   
   

def SignUp(request):
   if request.method == 'POST':
      uname = request.POST.get('Name')
      uemail = request.POST.get('Email_addr')
      pass1 = request.POST.get('pass') 

      my_user = User.objects.create_user(uname , uemail , pass1)
      my_user.save()
      login(request , my_user)
      return redirect('Blogs')
   
   return render(request,'SignUp.html')



def LogIn(request):
   if request.method == 'POST':
      uname = request.POST.get('Name')
      pass1 = request.POST.get('pass') 

      user = authenticate(request , username = uname , password = pass1)
      if user is not None:
         login(request , user)
         return redirect('Blogs')
      else:
         return HttpResponse("Username or password is incorrect!")


   return render(request,'LogIn.html')


def LogOut(request):
   if request.method =='POST':
      logout(request)
      return redirect('LogIn')