from account.models import User  # 필요한 모델을 가져옵니다.

# [nullvuild][COMMON-0001] 여기에 추가하고, setting.py에 추가하면 이 함수는 계속 실행됨
def custom_user_context(request):
    custom_user = None
    user_id = request.session.get('user')
    if user_id:
        try:
            custom_user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            custom_user = None
    return {'custom_user': custom_user}