from django.contrib import admin
from .models import FoodList, Question

class QuestionAdmin(admin.ModelAdmin):
    ordering = ['-created_at']  # Answer 모델의 created_at 필드를 기준으로 정렬
    list_display = ('title', 'created_at', 'answer')  # 리스트에 표시할 필드 설정

admin.site.register(Question, QuestionAdmin)

class FoodListAdmin(admin.ModelAdmin):
    list_display = ['name', 'main', 'soup', 'Spicy', 'temperature', 'weight', 'approved']
    list_filter = ['main', 'soup', 'Spicy', 'temperature', 'weight', 'approved']
    
    # approve_selected 액션
    def approve_selected(self, request, queryset):
        queryset.update(approved=True)
    approve_selected.short_description = "승인"
    
    # delete_selected 액션
    def delete_selected(self, request, queryset):
        queryset.delete()
    delete_selected.short_description = "삭제"
    
    actions = [approve_selected, delete_selected]

    ordering = ['-approved'] # 기본 정렬 순서

admin.site.register(FoodList, FoodListAdmin)

