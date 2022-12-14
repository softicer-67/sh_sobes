from django.db import models
from rest_framework.reverse import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={'pk': self.pk})


class Question(models.Model):
    question = models.TextField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')
    answer = models.TextField(null=True, blank=True)
    image = models.ImageField('Фото', upload_to='images/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.question

    # def get_absolute_url(self):
    #     return reverse('answer', kwargs={'answer_slug': self.slug})

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
