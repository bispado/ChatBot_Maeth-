from django.db import models

# Create your models here.

class Message(models.Model):
    body = models.TextField(null=False, blank=False, max_length=1000)
    sent = models.DateField(null=False, auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
