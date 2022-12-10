from django.urls import path, include
from rest_framework import routers

from lesson import views
from lesson.views import CategoryViewSet, QuestionViewSet


router = routers.DefaultRouter()
router.register(r'cat', CategoryViewSet)
router.register(r'quest', QuestionViewSet)


urlpatterns = [
    path('', views.index, name='home'),
    path("", include(router.urls))
]
