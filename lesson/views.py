from django.shortcuts import render
from rest_framework import mixins
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from lesson.serializers import QuestionSerializer, CategorySerializer
from .models import Question, Category


def index(request):
    cats = Category.objects.all()
    context = {
        'cats': cats,
    }
    return render(request, 'lesson/index.html', context=context)


def show_category(request, pk):
    w = Category.objects.get(pk=pk)
    c = w.question_set.all()
    return render(request, 'lesson/category.html', {'category': c})


def answer(request, question_slug):
    ans = get_object_or_404(Question, slug=question_slug)
    context = {
        'answer': ans
    }
    return render(request, 'lesson/answer.html', context=context)


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class CategoryViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer






