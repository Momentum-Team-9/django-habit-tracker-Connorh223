from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import constraints
from django.db.models.fields import CharField, DateTimeField

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"
    def __str__(self):
        return self.username

class Habit(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    goal = models.CharField(max_length=250, null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='habits')

    def __str__(self):
        return f'{self.goal}'

class DailyResult(models.Model):
    date = models.DateTimeField(default=date.today)
    results = models.PositiveIntegerField()
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='results', null=True)

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['habit', 'date'], name='unique_record')]