from django.contrib import admin

from .models import TestCategory, Subject, Topic, Choice, Question, QuestionType, Attempt


@admin.register(TestCategory)
class TestCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    list_display_links = ['id']
    list_editable = ['title', 'description']


class TopicInSubjectInline(admin.TabularInline):
    model = Topic


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_active']
    list_display_links = ['id']
    list_editable = ['title', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title']

    inlines = [TopicInSubjectInline]


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'title']
    list_display_links = ['id', 'subject']
    list_editable = ['title']
    search_fields = ['title']


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'subject', 'topic', 'number_of_questions', 'time_limit', 'result', 'is_completed']
    list_filter = ['is_completed']
    readonly_fields = ['student', 'subject', 'topic', 'number_of_questions', 'time_limit', 'result']


@admin.register(QuestionType)
class QuestionTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'prompt']
    list_display_links = ['title']
    list_editable = ['prompt']
    search_fields = ['title', 'prompt']


class ChoiceInQuestion(admin.TabularInline):
    model = Choice


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'topic', 'question']
    list_display_links = ['id', 'subject']
    list_editable = ['topic', 'question']
    search_fields = ['question']
    
    inlines = [ChoiceInQuestion]
