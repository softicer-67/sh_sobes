from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from lesson.serializers import QuestionSerializer, CategorySerializer
from .models import Question, Category


def index(request):
    data = {
        'categories': Category.objects.all(),
        'questions': Question.objects.all()
    }
    return render(request, 'lesson/index.html', data)


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class CategoryViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer






