from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

# [nullvuild] for user
from django.http import HttpResponseRedirect
from account.models import User

# [nullvuild] for auth
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password #비밀번호 암호화 / 패스워드 체크(db에있는거와 일치성확인)
from account.models import User #User table 참고

# Create your views here.
def index(request):
    template = loader.get_template('account_index.html')
    context = {}
    return HttpResponse(template.render(context, request))



def signup(request):
  #1. submit signup
  if request.method == 'POST': # 회원정보 저장    singup
    userid = request.POST.get('userid')
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    introduction = request.POST.get('introduction')
    
    pwd = make_password(pwd)
    user = User(userid=userid, name=name, pwd=pwd, introduction=introduction)
    user.save()
    return redirect('index')
  else:
    return render(request, 'account_signup.html')


'''
체크부터 검증좀..
그냥 == 하면 되고
CHECK 함수 쓰면 안됨
https://infinitt.tistory.com/221
'''


def login(request):
    response_data = {}
    if request.method == "POST":
        in_username = request.POST.get('username', None)
        in_pwd = request.POST.get('password', None)


        if not (in_username and in_pwd):
            response_data['error']="아이디와 비밀번호를 모두 입력해주세요."
        else : 
            myuser = User.objects.get(userid=in_username) 
            #db에서 꺼내는 명령. Post로 받아온 username으로 , db의 username을 꺼내온다.
            if check_password(in_pwd, myuser.pwd):
                request.session['user'] = myuser.id
                #세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
                #세션 user라는 key에 방금 로그인한 id를 저장한것.
                return redirect('/')
            else:
                response_data['error'] = "비밀번호를 틀렸습니다."

        return render(request, 'account_login.html',response_data)
      
    elif request.method == "GET" :
        return render(request, 'account_login.html')

    

'''
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
'''

  
  
  