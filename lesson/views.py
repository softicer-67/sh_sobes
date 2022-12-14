from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from lesson.serializers import QuestionSerializer, CategorySerializer
from .models import Question, Category


def index(request):
    return render(request, 'lesson/index.html', {'cats': Category.objects.all()})


def answer(request, cat_id):
    w = Category.objects.get(pk=cat_id)
    x = w.question_set.all()
    return render(request, 'lesson/answer.html', {'questions': x})


def page_not_found(request, exeption):
    return render(request, '<h2>Страница не найдена</h2?')


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class CategoryViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer






