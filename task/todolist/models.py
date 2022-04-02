from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
