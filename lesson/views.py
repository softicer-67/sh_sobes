from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from lesson.serializers import QuestionSerializer, CategorySerializer
from .models import Question, Category
from django.views.generic import DetailView


def index(request):
    data = {
        'categories': Category.objects.all(),
        'questions': Question.objects.all()
    }
    return render(request, 'lesson/index.html', data)


class NewsDetailView(DetailView):
    model = Question
    template_name = 'lesson/answer.html'
    context_object_name = 'answer'


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class CategoryViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer






