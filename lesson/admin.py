from django.contrib import admin

from lesson.models import Question, Category


# admin.site.register(Question)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Question)
class AdAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'category', 'image']
    search_fields = ['question', 'answer']
