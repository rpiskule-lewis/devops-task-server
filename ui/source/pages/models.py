from django.db import models
from encrypted_fields import fields

# Create your models here.
class Task(models.Model):
    inputs = fields.EncryptedTextField()
    script = models.TextField()
