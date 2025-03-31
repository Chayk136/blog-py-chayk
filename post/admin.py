from django.contrib import admin
from .models import Post, PostAttachment, Comment
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import gettext_lazy as _

# Register your models here.

@admin.register(Post)
class CustomPostAdmin(TranslationAdmin):
    fieldsets = (
        (_('Автор'), {"fields": ( 'author',)}),
        (_('Информация поста (Русском)'), {"fields": ( 'title_ru', 'content_ru',)}),
        (_('Информация поста (Англиский)'), {"fields": ( 'title_en', 'content_en',)}),
        (_('Информация поста (Казахский)'), {"fields": ( 'title_kk', 'content_kk',)}),
        (_('Доп. ифно'), {"fields": ( 'time_stamp', 'edited',)}),
    )
    add_fieldsets = (
        (_('Автор'), {"fields": ( 'author',)}),
        (_('Информация поста (Русском)'), {"fields": ( 'title_ru', 'content_ru',)}),
        (_('Информация поста (Англиский)'), {"fields": ( 'title_en', 'content_en',)}),
        (_('Информация поста (Казахский)'), {"fields": ( 'title_kk', 'content_kk',)}),
    )
    list_display = ('author', 'title', 'content', 'time_stamp', 'edited')
    search_fields = ('title', 'content',)
    ordering = ('-time_stamp',)

    def get_fieldsets(self, request, obj = None):
        if obj:
            return self.fieldsets
        return self.add_fieldsets

@admin.register(PostAttachment)
class CustomPostAttachmentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Файлы для поста', {"fields": ('name','file',)}), 
        ('Пост', {"fields": ('post',)})
    )
    add_fieldsets = (
        ('Файлы для поста', {"fields": ('file',)}), 
        ('Пост', {"fields": ('post',)})
    )
    list_display = ('name','file', 'post')
    search_fields = ('post__title',)
    ordering = ('post',)

    def get_fieldsets(self, request, obj = None):
        if obj:
            return self.fieldsets
        return self.add_fieldsets

@admin.register(Comment)
class CustomCommentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Автор', {"fields": ('author',)}),
        ('Информация комментария на русском', {"fields": ('post', 'content',)}),
        ('Доп. ифно', {"fields": ( 'time_stamp',)}),
    )
    list_display = ('author','time_stamp',)
    search_fields = ('author__username',)
    ordering = ('-time_stamp',)
        
