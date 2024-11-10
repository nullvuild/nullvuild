from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

# [nullvuild] for user
from django.http import HttpResponseRedirect
from account.models import User

# [nullvuild] for autho
from django.contrib import auth

# Create your views here.
def index(request):
    template = loader.get_template('account_index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def login(request):
    #post 접속
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user  = auth.authenticate(request, userid=username, pwd=password)
        
        if user is not None :
          auth.login(request, user)
          return redirect('home')
    #일반 접속
    else:
        return render(request,'account_login.html')

def signup(request):
  #1. submit signup
  if request.method == 'POST': # 회원정보 저장    singup
    userid = request.POST.get('userid')
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    introduction = request.POST.get('introduction')
    
    user = User(userid=userid, name=name, pwd=pwd, introduction=introduction)
    user.save()
    return redirect('index')
  else:
    return render(request, 'account_signup.html')


