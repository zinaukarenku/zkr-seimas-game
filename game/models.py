from django.db import models


class Politician(models.Model):
    full_name = models.CharField(max_length=255, unique=True)
    photo_url = models.URLField()
    is_male = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name


class GameOverStatistics(models.Model):
    selected_politician = models.ForeignKey(Politician, on_delete=models.SET_NULL, null=True, blank=True,
                                            related_name='game_over_selected')
    correct_politician = models.ForeignKey(Politician, on_delete=models.SET_NULL, null=True, blank=True,
                                           related_name='game_over_correct')

    correct_count = models.PositiveIntegerField(default=0)

    user_ip = models.GenericIPAddressField()
    user_agent = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
