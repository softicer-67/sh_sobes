from django.contrib import admin

from lesson.models import Question, Category


# admin.site.register(Question)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'category', 'image']
    search_fields = ['question', 'answer']
    prepopulated_fields = {'slug': ('question',)}
