from django.db import models

# Create your models here.
class techCrunchHeadline(models.Model):
    title = models.CharField(max_length=200)
    url = models.TextField()

    def __str__(self):
        return self.title