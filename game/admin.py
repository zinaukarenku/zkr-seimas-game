from django.contrib import admin

from django.contrib.admin import ModelAdmin
from django.db.models import Count

from game.models import GameOverStatistics, Politician


@admin.register(Politician)
class PoliticianAdmin(ModelAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(incorrect_count=Count('game_over_correct'))

    list_display = ['full_name', 'photo_url', 'is_male', 'incorrect_count']

    def incorrect_count(self, obj):
        return obj.incorrect_count

    incorrect_count.admin_order_field = 'incorrect_count'


@admin.register(GameOverStatistics)
class GameOverStatisticsAdmin(ModelAdmin):
    list_display = ['selected_politician', 'correct_politician', 'correct_count', 'user_ip', 'user_agent', 'created_at']
    list_select_related = ['selected_politician', 'correct_politician']
