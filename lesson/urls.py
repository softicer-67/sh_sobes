from django.urls import path, include
from rest_framework import routers
from lesson.views import index, answer
from lesson.views import CategoryViewSet, QuestionViewSet


router = routers.DefaultRouter()
router.register(r'cat', CategoryViewSet)
router.register(r'quest', QuestionViewSet)


urlpatterns = [
    path('', index, name='home'),
    path('<cat_id>/', answer, name='answer'),
    path('', include(router.urls))
]
