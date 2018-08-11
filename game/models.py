from django.db import models


class Politician(models.Model):
    full_name = models.CharField(max_length=255, unique=True)
    photo_url = models.URLField()
    is_male = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name
