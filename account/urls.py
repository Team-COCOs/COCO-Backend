from django.urls import path
from .views import signout ,signupView, myinfo, signin

# django에서 경로를 명시할 때 urlpatterns 리스트의 패턴을 항상 참고한다

urlpatterns = [
    path('signup/', signupView.as_view()),
    path('signin/', signin),
    path('signout/',signout),
    path('myinfo/',myinfo.as_view()),
]