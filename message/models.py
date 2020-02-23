from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class message(models.Model):
    message_from = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='message_from')
    message_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='message_to')
    message = models.CharField(max_length=500)
    message_time = models.DateTimeField()

    def __str__(self):
        return self.message


