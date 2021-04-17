from django.contrib import admin
from .models import *


class QuestionsInline(admin.StackedInline):
    model = QuestionsAns


class QuizAdmin(admin.ModelAdmin):
    inlines = QuestionsInline,
    list_display = 'id', 'title',


class QuestionsAnsAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'test'


admin.site.register(QuizModel, QuizAdmin)
admin.site.register(QuestionsAns, QuestionsAnsAdmin)
