from django.contrib import admin
from .models import FoodList

class FoodListAdmin(admin.ModelAdmin):
    list_display = ['name', 'main', 'soup', 'Spicy', 'temperature', 'weight']
    list_filter = ['main', 'soup', 'Spicy', 'temperature', 'weight']
    actions = ['DB에 추가', 'DB에서 삭제']

    def accept_recommend(self, request, queryset):
        for food in queryset:
            food.accepted = True
            food.save()

    def reject_recommend(self, request, queryset):
        queryset.delete()

admin.site.register(FoodList, FoodListAdmin)