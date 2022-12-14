from django.urls import path, include
from rest_framework import routers
from lesson.views import index, show_category, answer
from lesson.views import CategoryViewSet, QuestionViewSet


router = routers.DefaultRouter()
router.register(r'cat', CategoryViewSet)
router.register(r'quest', QuestionViewSet)


urlpatterns = [
    path('', index, name='home'),
    path('<int:pk>/', show_category, name='category'),
    path('<slug:question_slug>/', answer, name='answer'),
    path('', include(router.urls))
]
