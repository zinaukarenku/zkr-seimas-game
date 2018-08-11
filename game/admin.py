from django.contrib import admin

from django.contrib.admin import ModelAdmin

from game.models import GameOverStatistics


@admin.register(GameOverStatistics)
class GameOverStatisticsAdmin(ModelAdmin):
    list_display = ['selected_politician', 'correct_politician', 'correct_count', 'user_ip', 'user_agent', 'created_at']
    list_select_related = ['selected_politician', 'correct_politician']
