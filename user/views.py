from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

# [nullvuild] for user
from django.http import HttpResponseRedirect
from user.models import User

# [nullvuild] for auth
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password #비밀번호 암호화 / 패스워드 체크(db에있는거와 일치성확인)
from user.models import User #User table 참고

# Create your views here.
def index(request):
    template = loader.get_template('user_index.html')
    context = {}
    return HttpResponse(template.render(context, request))



def signup(request):
  #1. submit signup
  if request.method == 'POST': # 회원정보 저장    singup
    user_handle = request.POST.get('user_handle')
    user_name = request.POST.get('user_name')
    user_pwd = request.POST.get('user_pwd')
    user_intro = request.POST.get('user_intro')
    
    user_pwd = make_password(user_pwd)
    user = User(user_handle=user_handle, user_name=user_name, user_pwd=user_pwd, user_intro=user_intro)
    user.save()
    return redirect('index')
  else:
    return render(request, 'user_signup.html')


'''
체크부터 검증좀..
그냥 == 하면 되고
CHECK 함수 쓰면 안됨
https://infinitt.tistory.com/221
'''


def login(request):
    response_data = {}
    if request.method == "POST":
        in_username = request.POST.get('user_name', None)
        in_pwd = request.POST.get('user_pwd', None)


        if not (in_username and in_pwd):
            response_data['error']="아이디와 비밀번호를 모두 입력해주세요."
        else : 
            myuser = User.objects.get(user_handle=in_username) 
            #db에서 꺼내는 명령. Post로 받아온 username으로 , db의 username을 꺼내온다.
            if check_password(in_pwd, myuser.user_pwd):
                request.session['user'] = myuser.id
                #세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
                #세션 user라는 key에 방금 로그인한 id를 저장한것.
                return redirect('/')
            else:
                response_data['error'] = "비밀번호를 틀렸습니다."

        return render(request, 'user_login.html',response_data)
      
    elif request.method == "GET" :
        return render(request, 'user_login.html')

def logout(request):
    # 세션 무효화
    auth.logout(request)
    # 로그아웃 후 리다이렉트할 페이지
    return redirect('/')


'''
def login(request):
    #post 접속
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user  = auth.authenticate(request, user_handle=username, user_pwd=password)
        
        if user is not None :
          auth.login(request, user)
          return redirect('home')
    #일반 접속
    else:
        return render(request,'user_login.html')
'''

  
  
  