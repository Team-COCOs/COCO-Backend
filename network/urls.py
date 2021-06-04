from django.urls import path
from .views import AccCreateAPIView, SoundCreateAPIView, SoundGetAPIView, AccGetAPIVIEW,CountGetAPI,ScoreGetAPI

# django에서 경로를 명시할 때 urlpatterns 리스트의 패턴을 항상 참고한다
app_name = 'network'

urlpatterns = [
  path('acc/', AccCreateAPIView.as_view()),
  path('sound/',SoundCreateAPIView.as_view()),
  path('sound/count/', SoundGetAPIView.as_view()),
  path('acc/count/', AccGetAPIVIEW.as_view()),
  path('count/',CountGetAPI.as_view()),
  path('score/',ScoreGetAPI.as_view())
]